from functools import wraps

from flask_login import current_user
from flask import redirect


def checkRole(*role):

    def wrapper(view_function):
        @wraps(view_function)
        def decorator(*args, **kwargs):
            if not(current_user.is_authenticated and current_user.role in role):
                return redirect("/")
            return view_function(*args, **kwargs)

        return decorator

    return wrapper

def checkBoosterRole():
    if current_user.is_authenticated:
        if current_user.role != "BOOSTER":
            return redirect("/")
        else:
            pass
    else:
        return redirect("/")

def check(function_to_decorate):
    def wrapper(self, *args, **kwargs):
        if current_user.is_authenticated:
            if current_user.role != "ADMIN":
                return redirect("/")
            else:
                function_to_decorate(self, *args, **kwargs)
        else:
            return redirect("/")


    return wrapper
