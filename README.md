# RiskLens

一个使用 Python 和 PySide6 构建的，用于模拟和可视化风险的桌面应用。

## ✨ 主要功能

- **动态模拟**: 根据用户设定的概率进行风险模拟。
- **实时图表**: 使用 Matplotlib 实时绘制风险等级历史图。
- **风险预警**: 当风险等级超过阈值时，弹出预警提示。
- **数据记录**: 将模拟历史记录到 SQLite 数据库。
- **独立运行**: 已打包为独立的 Windows 可执行文件。

## 🛠️ 技术栈

- **GUI**: PySide6
- **图表**: Matplotlib
- **打包**: PyInstaller

## 🚀 运行与构建

1.  **安装依赖**

    ```bash
    pip install -r requirements.txt
    ```

2.  **从源码运行**

    ```bash
    python main.py
    ```

3.  **构建可执行文件**
    ```bash
    pyinstaller --name RiskLens --windowed --onefile --icon=icons/icon2.ico --add-data "icons;icons" --collect-all PySide6 main.py
    ```

## 🙏 致谢

- 图标素材来源于 [阿里巴巴矢量图标库](https://www.iconfont.cn/)。
