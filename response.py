def response_builder(status, response_headers, body):
    # if isinstance(body, str):
    #     body = body.encode()
    response = (
        f"{status}\r\n"
        f"Content-Type: {response_headers['Content-Type']}\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"\r\n"
    ).encode()
    return response+body