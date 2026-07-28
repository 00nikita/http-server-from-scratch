from handlers import (
    home,
    about,
    login_page,
    process_login,
    welcome,
    serve_static_file
)
routes = {
    ("GET", "/"): home,
    ("GET", "/about"): about,
    ("GET", "/login"): login_page,
    ("POST", "/login"): process_login,
    ("GET", "/welcome"): welcome
}

def resolve(method, path):
    if method == "GET" and path.startswith("/static/"):
        return serve_static_file
    return routes.get((method, path))