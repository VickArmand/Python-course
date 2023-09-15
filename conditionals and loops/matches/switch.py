# matches are similar to switch in c
def http_error(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"