# TR5-Simulator - 5-Trade Strategy Simulation App

> **TR5-Simulator** is a professional trading strategy simulator designed to model a 5-trade-per-day system with dynamic risk management and equity curve analysis.  
> Built with **Streamlit**, it enables traders to intuitively understand the effects of Winrate, Risk/Reward ratios, and daily risk exposure through interactive simulations.

Users can either run the provided standalone executable or run the Python source code directly.

---

## ✨ Key Features

- Simulate 5 consecutive trades daily with progressive risk scaling
- Customize simulation parameters:
  - **Winrate** (0.1 to 0.9)
  - **Risk:Reward ratio** (1.0 to 5.0)
  - **Total daily risk percentage**
  - **Number of trading days**
  - **Number of simulation runs**
- Visualize results:
  - **Equity Curve** progression
  - **Maximum Drawdown** distribution
- Calculate:
  - **Expectancy per trade**
  - **Average maximum drawdown**
  - **Probability of exceeding 20% drawdown**
- Built-in real-time server stop/reconnect functionality

---

## 🚀 How to Use

### For Regular Users

_No Python installation is required._

1. Download the executable file from the `dist/` folder (`run_app.exe`).
2. Double-click on `run_app.exe` to start the simulator.
3. The app will automatically open in your default browser (typically at [http://localhost:8501](http://localhost:8501)).

> 📌 **Note:** If Windows Defender SmartScreen appears, click **More Info → Run Anyway** to proceed.

---

### For Developers

If you want to run the source code manually:

#### Prerequisites

- Python 3.8+
- pip package manager

#### Installation

```bash
pip install -r requirements.txt
```

#### Running the app

```bash
streamlit run mo_phong_dashboard_chien_luoc.py
```

The application will open automatically at [http://localhost:8501](http://localhost:8501).

---

## 🧠 Simulation Logic Overview

- Each day consists of 5 progressive trades.
- Dynamic risk adjustment after each trade outcome.
- Profits and losses modify the next risk exposure.
- The system records Equity Curve and Maximum Drawdown statistics across multiple simulation runs.

---

## 📁 Project Structure

```
TR5-Simulator/
├── build/                     → Temporary build artifacts
├── dist/run_app.exe            → Standalone executable
├── mo_phong_dashboard_chien_luoc.py → Main Streamlit application
├── run_app.py                  → Alternative entry point (optional)
├── run_app.spec                → PyInstaller configuration file
├── requirements.txt            → Python dependency list
└── readme.txt                  → Legacy description draft
```

---

## 🛠 Deployment Options

- Local deployment via Python & Streamlit
- Executable `.exe` distribution (via PyInstaller)
- Optional: Deploy to cloud platforms (Streamlit Cloud, AWS)

---

## 🌟 Acknowledgements

Developed as part of a trading strategy research and educational project.  
Special thanks to all contributors for simulation modeling, UI design, and testing efforts.

---

## 📄 License

This project is licensed under the MIT License.  
See the `LICENSE` file for more details.