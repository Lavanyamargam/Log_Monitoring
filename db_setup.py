import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# Create table to store logs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS error_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        error_type TEXT,
        log_message TEXT
    )
''')

conn.commit()
conn.close()
print("logs.db and table created successfully.")
