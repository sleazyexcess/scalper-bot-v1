import streamlit as st

# Sidebar navigation to organize your bot's features
page = st.sidebar.selectbox("Dashboard Menu", ["Control Panel", "Settings", "Performance Logs"])

if page == "Control Panel":
    st.title("Simple Scalper Control Panel")
    st.write("Manage your real-time trading parameters here.")
    
    # Core trading inputs
    lot_size = st.number_input("Lot Size", min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    
    if st.button("Activate Scalper"):
        st.success("Scalper Activated with " + str(lot_size) + " lot size.")

elif page == "Settings":
    st.title("Bot Settings")
    st.write("Configure risk management parameters.")
    
    tp = st.number_input("Take Profit (pips)", value=20)
    sl = st.number_input("Stop Loss (pips)", value=10)
    max_risk = st.slider("Max Risk per Trade (%)", 0.1, 5.0, 1.0)

elif page == "Performance Logs":
    st.title("Performance Logs")
    st.write("Monitor your trade history and bot activity.")
    st.info("No active trades found. Connect your MT5 terminal to begin.")
