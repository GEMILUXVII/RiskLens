# <div align="center"> RiskLens </div>

<div align="center"> <em> A Monte Carlo Simulation Tool for Risk Analysis </em> </div>

<br>

<div align="center">
  <a href="#"><img src="https://img.shields.io/badge/version-v0.1.0--alpha-9644F4?style=for-the-badge" alt="Version"></a>
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-E53935?style=for-the-badge" alt="License"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version"></a>
</div>

<div align="center">
  <a href="#"><img src="https://img.shields.io/badge/platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Support"></a>
  <a href="#"><img src="https://img.shields.io/badge/updated-2025--06--22-0097A7?style=for-the-badge&logo=calendar&logoColor=white" alt="Last Updated"></a>
</div>

## 📖 关于项目 (About This Project)

这是一个为朋友的课程设计而创建的简单的蒙特卡洛模拟小工具，主要用于功能演示

This is a simple Monte Carlo simulation small tool created for a friend's course project. It is intended for academic exchange and functional demonstration purposes.

---

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
