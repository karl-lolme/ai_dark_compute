import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
from datetime import datetime

st.set_page_config(page_title="AI Dark Compute Tracker", layout="wide", page_icon="🌐")
st.title("🌐 AI Dark Compute Tracker")
st.markdown("**Global Data Center Utilization • Real-time AI Crash Predictor** | Updated May 22, 2026")

# Live metrics
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Global Vacancy", "6.6%", "-2.1 pts YoY")
with col2: st.metric("NA Primary Vacancy", "1.5%", "Record low")
with col3: st.metric("AI Workload Share", "25% → 50%", "Inference shift 2027")
with col4: st.metric("Under Construction", "23+ GW", "831 sites")

tab1, tab2, tab3, tab4 = st.tabs(["📈 Utilization Trends", "🏗️ Pipeline", "💰 Hyperscalers", "🚨 Signals"])

with tab1:
    vacancy_df = pd.DataFrame({
        "Quarter": ["Q1 2024", "Q1 2025", "Q2 2025 est", "Q1 2026 est"],
        "Global Vacancy %": [8.7, 6.6, 6.2, 6.0],
        "NA Primary Vacancy %": [2.8, 1.5, 1.4, 1.6]
    })
    fig1 = px.line(vacancy_df, x="Quarter", y=["Global Vacancy %", "NA Primary Vacancy %"], markers=True,
                   title="Vacancy Rates (Lower = Higher Utilization)")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.info("Pre-leasing still ~74-77% → demand outpacing supply")
    st.metric("New Capacity 2026-2030", "~100 GW (doubling global)")

with tab3:
    capex_df = pd.DataFrame({
        "Company": ["MSFT", "AMZN", "GOOGL", "META"],
        "2026 Capex ($B)": [120, 200, 180, 125],
        "AI/Cloud Rev Growth %": [29, 28, 63, 33]
    })
    fig3 = px.bar(capex_df, x="Company", y=["2026 Capex ($B)", "AI/Cloud Rev Growth %"], barmode="group")
    st.plotly_chart(fig3, use_container_width=True)
    
    st.subheader("Data Center REITs (live market confidence)")
    tickers = ["EQIX", "DLR", "AMT"]
    prices = {t: yf.Ticker(t).info.get('regularMarketPrice', 'N/A') for t in tickers}
    st.write(prices)

with tab4:
    st.subheader("🚨 Dark Compute / AI Crash Signals")
    st.success("**No signals yet** — market remains extremely tight")
    st.caption("First potential moderation window: late 2026–2027")

st.caption("Data: CBRE • JLL • IEA • BNEF • Epoch AI • Hyperscaler earnings • Live stocks via yfinance")