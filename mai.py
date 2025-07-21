from log_parser import extract_error_type, extract_timestamp, insert_to_db
from alert_email import send_alert

LOG_FILE_PATH = "logs/sample_log.txt"

with open(LOG_FILE_PATH, "r") as file:
    for line in file:
        error_type = extract_error_type(line)
        if error_type:
            timestamp = extract_timestamp(line)
            insert_to_db(timestamp, error_type, line)

            if error_type == "CRITICAL":
                send_alert(line)  # Send email alert for CRITICAL errors

print("Log processing complete. Errors stored in database.")

