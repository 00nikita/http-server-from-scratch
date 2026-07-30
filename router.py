from handlers import (
    home,
    about,
    login_page,
    process_login,
    welcome,
    serve_static_file,
)
routes = {
    "/": 
    {
        "GET": home,
        "HEAD": home,
    },
    "/about":
    {
        "GET": about,
        "HEAD": about,
    },
    "/login":
    {
        "GET": login_page,
        "POST": process_login,
        "HEAD": login_page,
    },
    "/welcome":
    {
        "GET": welcome,
        "HEAD": welcome,
    }
}

def resolve(method, path):
    if method in ("GET", "HEAD") and path.startswith("/static/"):
        return serve_static_file
    route = routes.get(path)
    if route:
        handler = route.get(method)
        if handler:
            return handler, route
        return None, route

    return None, None