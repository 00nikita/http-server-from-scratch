def parse_request(request):
    request_line = request.splitlines()[0]
    method, path, version = request_line.split()
    query_param = {}
    if "?" in path:
        path, query = path.split("?", 1)
        for pair in query.split("&"):
            key, value = pair.split("=")
            query_param[key] = value
    request_lines = crequest.splitlines()
    headers = {}
    for line in request_lines[1:]:
        if line=="":
            break
        key, value = line.split(":", 1)
        headers[key]=value.strip()
    return method, path, version, query_param, headers