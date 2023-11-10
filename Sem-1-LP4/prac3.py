import re

# Sample log data (you can replace this with real log data)
log_data = """
2023-10-19 10:05:25 - User login successful: username=user1
2023-10-19 10:06:12 - File accessed: filename=important.doc
2023-10-19 10:06:45 - User login successful: username=user2
2023-10-19 10:07:30 - File accessed: filename=confidential.pdf
"""

# Define patterns to capture specific events
login_pattern = r"User login successful: username=(\w+)"
file_access_pattern = r"File accessed: filename=(\w+)"

# Initialize empty lists to store events
login_events = []
file_access_events = []

# Split log data into lines
log_lines = log_data.strip().split('\n')

# Process each log line and extract events
for line in log_lines:
    if re.search(login_pattern, line):
        match = re.search(login_pattern, line)
        username = match.group(1)
        login_events.append(f"User '{username}' logged in.")

    if re.search(file_access_pattern, line):
        match = re.search(file_access_pattern, line)
        filename = match.group(1)
        file_access_events.append(f"File '{filename}' was accessed.")

# Correlate events
for login_event in login_events:
    for file_access_event in file_access_events:
        print(f"Correlation: {login_event} - {file_access_event}")
