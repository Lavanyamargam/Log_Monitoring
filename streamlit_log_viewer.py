import streamlit as st
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

# Load logs into pandas DataFrame
df = pd.read_sql_query("SELECT * FROM error_logs ORDER BY timestamp DESC", conn)

st.title("🛠️ Log Monitoring Dashboard")
st.markdown("View application errors and critical system logs")

# Filter by error type
error_type = st.selectbox("Filter by Error Type", options=["ALL", "WARNING", "ERROR", "CRITICAL"])

if error_type != "ALL":
    df = df[df['error_type'] == error_type]

# Display the filtered table
st.dataframe(df)

# Show total count
st.markdown(f"### Total Records: {len(df)}")

conn.close()
