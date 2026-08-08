def is_authenticated(headers):
    auth_header = headers.get("Authorization")
    if not auth_header:
        return False
    return True