import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import os

# Tính expectancy
def calculate_expectancy(winrate, rr):
    return (winrate * rr) - ((1 - winrate) * 1)

# Mô phỏng chiến lược 5 lệnh với quản trị rủi ro như mô tả
def simulate_equity(winrate, rr, total_risk_pct, days, sims, balance_start=1000):
    equity_curves = []
    max_drawdowns = []

    for _ in range(sims):
        balance = balance_start
        curve = []
        peak = balance
        max_dd = 0

        for _ in range(days):
            part = total_risk_pct / 3 / 100 * balance  # mỗi phần rủi ro

            # L1
            r1 = 0.5 * part
            p1 = r1 * rr if random.random() < winrate else -r1

            # L2
            r2 = 1 * part
            p2 = r2 * rr if random.random() < winrate else -r2

            # L3
            r3 = 1.5 * part
            p3 = r3 * rr if random.random() < winrate else -r3

            trades = [p1, p2, p3]
            profit_3 = sum(trades)

            if all(p < 0 for p in trades):
                balance += profit_3
                curve.append(balance)
                peak = max(peak, balance)
                max_dd = max(max_dd, (peak - balance) / peak)
                continue

            # L4
            if profit_3 > 0:
                r4 = profit_3
                p4 = r4 * rr if random.random() < winrate else -r4
                trades.append(p4)

                if p4 < 0:
                    balance += sum(trades)
                    curve.append(balance)
                    peak = max(peak, balance)
                    max_dd = max(max_dd, (peak - balance) / peak)
                    continue

                # L5
                profit_4 = sum(trades)
                r5 = 0.5 * profit_4
                p5 = r5 * rr if random.random() < winrate else -r5
                trades.append(p5)

            balance += sum(trades)
            curve.append(balance)
            peak = max(peak, balance)
            max_dd = max(max_dd, (peak - balance) / peak)

        equity_curves.append(curve)
        max_drawdowns.append(max_dd)

    return equity_curves, max_drawdowns
#Khởi giá trị stopped nếu chưa có
if 'stopped' not in st.session_state:
    st.session_state.stopped = False

#Nếu url có ?rerun=true sex reset stopped
params = st.experimental_get_query_params()
if params.get("rerun") == ["true"]:
    st.session_state.stopped = False
    #Xóa params để ko loop
    st.experimental_set_query_params()
#Nếu đã stopped thì show Reconnect Button
if st.session_state.stopped:
    st.set_page_config(page_title="📊 Mô phỏng chiến lược 5 lệnh", layout="wide")
    st.title("🚫 Server đã tạm dừng")
    st.write("Please 🔄 Reconnect to continue.")
    if st.button("🔄 Reconnect"):
        # Thêm ?rerun=true vào URL, Streamlit sẽ tự load lại
        st.experimental_set_query_params(rerun="true")
    st.stop()

# Giao diện
st.title("📊 Mô phỏng chiến lược giao dịch 5 lệnh/ngày")

with st.sidebar:
    # Stop server button
    if st.button("🛑 Stop server"):
        st.session_state.stopped = True
        st.experimental_set_query_params(rerun="true")
        st.stop()

    winrate = st.slider("Tỷ lệ Winrate", 0.1, 0.9, 0.5, 0.01)
    rr = st.slider("Risk : Reward", 1.0, 5.0, 2.0, 0.1)
    total_risk = st.slider("Tổng rủi ro mỗi ngày (%)", 1, 10, 3)
    days = st.slider("Số ngày giao dịch", 50, 300, 100, 10)
    sims = st.slider("Số lần mô phỏng", 100, 1000, 200, 100)
    run = st.button("🚀 Chạy mô phỏng")

if run:
    eq_curves, drawdowns = simulate_equity(winrate, rr, total_risk, days, sims)

    st.subheader("📈 Biểu đồ Equity Curve")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    for c in eq_curves[:30]:
        ax1.plot(c, alpha=0.4)
    ax1.set_title("Equity Curve (30 lần mô phỏng đầu)")
    ax1.set_xlabel("Ngày")
    ax1.set_ylabel("Số dư")
    st.pyplot(fig1)

    st.subheader("📉 Phân phối Max Drawdown (%)")
    fig2, ax2 = plt.subplots()
    ax2.hist([dd * 100 for dd in drawdowns], bins=30, edgecolor="black")
    ax2.set_title("Phân phối Max Drawdown")
    ax2.set_xlabel("Max DD (%)")
    ax2.set_ylabel("Số lần mô phỏng")
    st.pyplot(fig2)

    expectancy = calculate_expectancy(winrate, rr)
    st.metric("📊 Expectancy", f"{expectancy:.2f} per trade")

    st.metric("🔥 Max DD trung bình", f"{np.mean(drawdowns) * 100:.2f}%")
    st.metric("🚨 Tỷ lệ bị DD > 20%", f"{np.mean([dd > 0.2 for dd in drawdowns]) * 100:.2f}%")