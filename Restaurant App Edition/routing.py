from controllers import register, login , register_admin,login_admin


routing_path = {
    'login': login,
    'register': register,
    'register_admin':register_admin,
    'login_admin':login_admin



}


def find_route(route):
    if route in routing_path:
        return routing_path[route]
    else:
        raise ValueError("cant find route.404")
