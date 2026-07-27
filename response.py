from datetime import datetime, timezone

def response_builder(status, response_headers, body):
    now = datetime.now(timezone.utc)
    date = now.strftime("%a, %d %b %Y %H:%M:%S GMT")

    response = (
        f"{status}\r\n"
        f"Content-Type: {response_headers['Content-Type']}\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Server: NikhithaHTTP/1.0\r\n"
        f"Date: {date}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    ).encode()
    return response+body