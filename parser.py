def parse_request(request):
    request_line = request.splitlines()[0]
    method, path, version = request_line.split()
    query_param = {}
    if "?" in path:
        path, query = path.split("?", 1)
        for pair in query.split("&"):
            key, value = pair.split("=")
            query_param[key] = value
    request_lines = request.splitlines()
    headers = {}
    for line in request_lines[1:]:
        if line=="":
            break
        key, value = line.split(":", 1)
        headers[key]=value.strip()
    body = {}
    if request_lines[request_lines.index("")+1]: # Check if there's a body
        body_lines = request_lines[request_lines.index("")+1]
        for pair in body_lines.split("&"):
            key, value = pair.split("=")
            body[key] = value
    return method, path, version, query_param, headers, body