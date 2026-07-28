from datetime import datetime, timezone

def response_builder(status, response_headers, body):
    response = status + "\r\n"
    for header, value in response_headers.items():
        response += f"{header}: {value}\r\n"
    response += "\r\n"
    return response.encode() + body