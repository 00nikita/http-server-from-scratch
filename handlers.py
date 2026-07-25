def home():
    with open("pages/index.html") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def about():
    with open("pages/about.html") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def login_page():
    with open("pages/login.html") as f:
        page = f.read()
    return "HTTP/1.1 200 OK", page
def process_login(headers, body):
    with open("pages/login_success.html") as f:
        page = f.read()
    username = body["username"]
    page = page.replace("{{username}}", username)
    return "HTTP/1.1 200 OK", pagec
def not_found():
    with open("pages/not_found.html") as f:
        page = f.read()
    return "HTTP/1.1 404 Not Found", page