# TR5-Simulator - 5-Trade Strategy Simulation App

**TR5-Simulator** is a trading strategy simulator that models a 5-trade-per-day system with dynamic risk management and equity curve analysis. Built with **Streamlit**, the application allows traders to understand the effects of winrate, risk/reward ratios, and daily risk exposure over time through interactive simulations.

Users can either run the standalone executable provided, or developers can run the Python source code directly.

---

## ✨ Key Features

- Simulate 5 consecutive trades daily with progressive risk scaling
- Customize:
  - Winrate (0.1 to 0.9)
  - Risk:Reward ratio (1.0 to 5.0)
  - Total daily risk percentage
  - Number of trading days
  - Number of simulation runs
- Visualize:
  - Equity Curve progression
  - Maximum Drawdown distribution
- Calculate expectancy, average drawdowns, and risk probabilities
- Built-in real-time server stop/reconnect functionality for smoother usage

---

## 🚀 How to Use

### For Regular Users

No Python installation is required.

1. Download the executable from the `dist/` folder (`run_app.exe`).
2. Double-click `run_app.exe` to launch the TR5-Simulator.
3. The app will open automatically in your default browser (typically at `http://localhost:8501`).

> 📌 **Note:** If Windows Defender SmartScreen appears, click **"More Info" → "Run Anyway"** to proceed.


### For Developers

If you prefer running from the source code or modifying it, follow these steps:

#### Prerequisites
- Python 3.8+
- pip package manager

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Run the app locally

```bash
streamlit run mo_phong_dashboard_chien_luoc.py
```

The app will open at `http://localhost:8501` by default.

---

## 🧠 Simulation Logic Overview

- Each day consists of 5 progressive trades.
- Risk management adjusts after every trade based on the result.
- Profit/loss directly affects the next trade's risk exposure.
- The app tracks the equity curve and maximum drawdowns across multiple simulation runs to provide comprehensive performance statistics.

---

## 📁 Project Structure

```
TR5-Simulator/
├── build/                    → Temporary build artifacts (auto-generated)
├── dist/run_app.exe           → Standalone executable for users
├── mo_phong_dashboard_chien_luoc.py → Main Streamlit app source code
├── run_app.py                 → Alternative entry point (optional)
├── run_app.spec               → PyInstaller configuration file
├── requirements.txt           → List of Python dependencies
└── readme.txt                 → Draft project description (legacy)
```

---

## 🛠 Deployment

- Local execution (via Streamlit)
- Standalone executable (via PyInstaller)
- Optional cloud deployment (e.g., Streamlit Cloud, AWS, etc.) with minor adjustments

---

## 🌟 Acknowledgements

Developed as part of a trading strategy research project. Thanks to the development team for contributions in simulation logic design, testing, and optimization.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for full details.