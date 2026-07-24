def parse_request(request):
    headers_part, body_part = request.split("\r\n\r\n", 1)
    request_line, header_lines = headers_part.split("\r\n", 1)
    method, path, version = request_line.split()
    query_param = {}
    if "?" in path:
        query = path.split("?", 1)
        for pair in query[1].split("&"):
            key, value = pair.split("=")
            query_param[key] = value.strip()
    headers = {}
    for line in header_lines.split("\r\n"):
        key, value = line.split(": ", 1)
        headers[key] =  value.strip()
    body = {}
    if body_part:
        for line  in body_part.split("&"):
            key, value = line.split("=")
            body[key] = value.strip()

    return method, path, version, query_param, headers, body