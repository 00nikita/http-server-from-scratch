from datetime import datetime

def log_access(client_ip, method, path, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("access.log", "a") as log_file:
        log_file.write(f"{timestamp} | {client_ip} | {method} | {path} | {status}\n")

def log_error(client_ip, method, path, status, error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("error.log", "a") as log_file:
        log_file.write(f"{timestamp} | {client_ip} | {method} | {path} | {status} | {error}\n")