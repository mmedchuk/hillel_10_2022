from functools import wraps


# MODIFY THIS DECORATOR
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        _to_be_reversed = func(*args, **kwargs)
        if isinstance(_to_be_reversed, str):
            return _to_be_reversed[::-1]
        return None

    return wrapper


# TARGET FUNCTIONS
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"


@reverse_string
def get_university_founding_year() -> int:
    return 1957


# TEST OUPUT
print(get_university_name(), get_university_founding_year(), sep="\n")
