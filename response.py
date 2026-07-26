def response_builder(status, response_headers, body):
    headers = f"{status}\r\nContent-Type: {response_headers['Content-Type']}\r\nContent-Length: {len(body)}\r\n\r\n"
    if isinstance(body, bytes):
        return headers.encode()+ body
    else:
        return headers.encode()+ body.encode()
