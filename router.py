from handlers import (
    home,
    about,
    login_page,
    process_login,
    welcome,
    serve_static_file
)
routes = {
    "/": 
    {
        "GET": home
    },
    "/about":
    {
        "GET": about
    },
    "/login":
    {
        "GET": login_page,
        "POST": process_login
    },
    "/welcome":
    {
        "GET": welcome
    }
}

def resolve(method, path):
    if method == "GET" and path.startswith("/static/"):
        return serve_static_file
    route = routes.get(path)
    if route:
        handler = route.get(method)
        if handler:
            return handler, route
        return None, route

    return None, None