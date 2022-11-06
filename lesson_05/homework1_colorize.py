font_color: dict = {
    "GREY": "\033[90m",
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "PINK": "\033[95m",
    "TURQUOSE": "\033[96m",
    "END": "\033[0m",
}


class Colorizer:
    """Selection font color"""

    def __init__(self, color="END"):
        self.color: str = color

    def __enter__(self):
        if self.color.upper() in font_color:
            print(f"{font_color[self.color.upper()]}", end="")

    def __exit__(self, tp, vl, tb):
        print(f"{font_color['END']}", end="")


with Colorizer():
    print("aaa")
    print("bbb")
    print("ccc")
