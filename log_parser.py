import re
import sqlite3

# Step 1: Function to detect error type from log line
def extract_error_type(log_line):
    pattern = r"(WARNING|ERROR|CRITICAL)"
    match = re.search(pattern, log_line)
    if match:
        return match.group(1)  # Return the error type
    return None

# Step 2: Extract timestamp
def extract_timestamp(log_line):
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    match = re.search(pattern, log_line)
    if match:
        return match.group(0)
    return "Unknown"

# Step 3: Save to database
def insert_to_db(timestamp, error_type, message):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO error_logs (timestamp, error_type, log_message) VALUES (?, ?, ?)",
                   (timestamp, error_type, message.strip()))
    conn.commit()
    conn.close()
