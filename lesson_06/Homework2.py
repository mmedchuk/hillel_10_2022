# Replace dict value decorator
# MODIFY THIS DECORATOR

from functools import wraps


def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):
            _data = func(*args, **kwargs)
            if target_key not in _data:
                raise ValueError("Wrong key")
            else:
                _data[target_key] = replace_with
            return _data

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUTPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
