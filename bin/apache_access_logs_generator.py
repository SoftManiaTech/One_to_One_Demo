import random
import time
from datetime import datetime

# List of simulated IPs and URLs for log generation
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1", "203.0.113.5", "198.51.100.7"]
urls = ["/home", "/about", "/contact", "/products", "/login", "/dashboard", "/search"]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
]

# Function to generate a single log entry
def generate_log_entry():
    ip = random.choice(ips)
    timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    request_method = random.choice(["GET", "POST"])
    url = random.choice(urls)
    status = random.choice(["200", "404", "500", "403", "302"])
    response_time = round(random.uniform(0.1, 1.5), 3)
    user_agent = random.choice(user_agents)
    
    log_entry = (
        f'{ip} - - [{timestamp}] "{request_method} {url} HTTP/1.1" {status} {random.randint(200, 1500)} '
        f'"-" "{user_agent}" {response_time}'
    )
    return log_entry

# Function to continuously write log entries to the file
def generate_logs():
    while True:
        log_entry = generate_log_entry()
        print(log_entry)  # Optional: print to console for monitoring
        time.sleep(random.uniform(0.5, 2.0))  # Simulate variable request intervals

# Run the log generator
if __name__ == "__main__":
    generate_logs()
