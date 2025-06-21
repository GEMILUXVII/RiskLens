import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QComboBox, QLabel, QPushButton, QSlider, QDoubleSpinBox, QMessageBox,
    QStatusBar
)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib

# 设置matplotlib支持中文的字体列表
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'FangSong', 'KaiTi', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

import matplotlib.ticker

from core.simulation import calculate_risk, get_random_location, get_current_time
from database.handler import log_simulation, init_db

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("简单风险模拟系统")
        self.setWindowIcon(QIcon(resource_path("icons/icon2.ico")))
        self.setGeometry(100, 100, 800, 600)

        self.risk_history = []
        self.simulation_count = 0

        # Initialize database
        init_db()

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # Left panel for controls
        controls_layout = QVBoxLayout()
        main_layout.addLayout(controls_layout)

        # Risk type selection
        risk_type_label = QLabel("选择风险类型:")
        self.risk_type_combo = QComboBox()
        self.risk_type_combo.addItems(["设备风险", "结构风险", "行为风险"])
        self.risk_type_combo.currentTextChanged.connect(self.update_responsible_person)
        controls_layout.addWidget(risk_type_label)
        controls_layout.addWidget(self.risk_type_combo)

        # Responsible person display
        self.responsible_person_label = QLabel("责任人: 设备管理员")
        controls_layout.addWidget(self.responsible_person_label)

        # Risk probability selection
        probability_label = QLabel("设置风险概率:")
        self.probability_slider = QSlider(Qt.Horizontal)
        self.probability_slider.setRange(0, 100)
        self.probability_slider.valueChanged.connect(self.update_probability_spinbox)
        self.probability_spinbox = QDoubleSpinBox()
        self.probability_spinbox.setRange(0.0, 1.0)
        self.probability_spinbox.setSingleStep(0.01)
        self.probability_spinbox.valueChanged.connect(self.update_probability_slider)
        controls_layout.addWidget(probability_label)
        controls_layout.addWidget(self.probability_slider)
        controls_layout.addWidget(self.probability_spinbox)

        # Simulation button
        simulate_button = QPushButton("点击模拟")
        simulate_button.clicked.connect(self.run_simulation)
        controls_layout.addWidget(simulate_button)

        controls_layout.addStretch()

        # Right panel for chart
        chart_layout = QVBoxLayout()
        main_layout.addLayout(chart_layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        chart_layout.addWidget(self.canvas)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.update_status_bar()

        self.plot_risk_history()

    def update_responsible_person(self, risk_type):
        responsible_persons = {
            "设备风险": "设备管理员",
            "结构风险": "技术负责人",
            "行为风险": "安全总监",
        }
        self.responsible_person_label.setText(f"责任人: {responsible_persons.get(risk_type)}")

    @Slot(int)
    def update_probability_spinbox(self, value):
        self.probability_spinbox.setValue(value / 100.0)

    @Slot(float)
    def update_probability_slider(self, value):
        self.probability_slider.setValue(int(value * 100))

    def run_simulation(self):
        risk_type = self.risk_type_combo.currentText()
        probability = self.probability_spinbox.value()

        risk_level = calculate_risk(risk_type, probability)
        location = get_random_location()
        timestamp = get_current_time()

        self.simulation_count += 1
        self.risk_history.append(risk_level)

        log_simulation(timestamp, location, risk_type, probability, risk_level)
        self.update_status_bar(location, timestamp)

        if risk_level >= 3:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("风险预警")
            msg_box.setText(f"检测到高风险！\n风险等级: {risk_level:.2f}")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowIcon(QIcon(resource_path("icons/icon2.ico")))
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()

        self.plot_risk_history()

    def plot_risk_history(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if self.risk_history:
            x_values = range(1, self.simulation_count + 1)
            y_values = self.risk_history
            ax.plot(x_values, y_values, marker='o', linestyle='-', color='dodgerblue', label='风险等级')
            ax.set_xlim(0.5, self.simulation_count + 0.5)
            ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
            ax.legend()
        else:
            ax.set_xlim(0, 10)

        ax.set_xlabel('模拟次数')
        ax.set_ylabel('风险等级')
        ax.set_ylim(0, 5.5)
        ax.set_title('风险等级历史记录')
        ax.grid(True, linestyle='--', alpha=0.6)
        
        self.canvas.draw()

    def update_status_bar(self, location=None, timestamp=None):
        location_text = f"地点: {location}" if location else ""
        time_text = f"时间: {timestamp}" if timestamp else ""
        self.status_bar.showMessage(f"{location_text} | {time_text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
