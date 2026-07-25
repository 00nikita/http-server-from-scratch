def response_builder(status, headers, body):
    content_type = headers.get("Content-Type", "text/html")
    return f"{status}\r\nContent-Type: {content_type}\r\nContent-Length: {len(body)}\r\n\r\n{body}"
