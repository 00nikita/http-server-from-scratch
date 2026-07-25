def response_builder(status, response_headers, body):
    return f"{status}\r\nContent-Type: {response_headers['Content-Type']}\r\nContent-Length: {len(body)}\r\n\r\n{body}"
