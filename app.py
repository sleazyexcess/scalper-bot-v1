import streamlit as st
import os

page = st.sidebar.selectbox("Dashboard Menu", ["Control Panel", "Settings", "Performance Logs"])

if page == "Control Panel":
    st.title("Simple Scalper Control Panel")
    
    # Status Indicator Logic
    if os.path.exists("logs.txt"):
        with open("logs.txt", "r") as f:
            status = f.readline().strip()
            if "Active" in status:
                st.success(f"Status: {status}")
            else:
                st.warning(f"Status: {status}")
    
    lot_size = st.number_input("Lot Size", min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    if st.button("Activate Scalper"):
        st.success(f"Command Sent: Scalper Activated at {lot_size} lots.")

elif page == "Settings":
    st.title("Bot Settings")
    tp = st.number_input("Take Profit (pips)", value=20)
    sl = st.number_input("Stop Loss (pips)", value=10)

elif page == "Performance Logs":
    st.title("Performance Logs")
    if os.path.exists("logs.txt"):
        with open("logs.txt", "r") as f:
            st.text_area("Live Logs", value=f.read(), height=200)
