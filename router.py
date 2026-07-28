from handlers import (
    home,
    about,
    login_page,
    process_login,
    welcome
)


routes = {
    ("GET", "/"): home,
    ("GET", "/about"): about,
    ("GET", "/login"): login_page,
    ("POST", "/login"): process_login,
    ("GET", "/welcome"): welcome
}