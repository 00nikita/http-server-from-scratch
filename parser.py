def parse_request(request):
    # Split the request into lines
    lines = request.splitlines()
    
    # Get the request line (the first line)
    request_line = lines[0]
    
    # Split the request line into method, path, and version
    method, path, version = request_line.split()
    
    # Create a dictionary to hold the headers
    headers = {}
    
    # Iterate over the remaining lines to extract headers
    for line in lines[1:]:
        if line:  # Ignore empty lines
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()
    
    return method, path, version, headers