from pathlib import Path
from typing import Generator

from pympler import asizeof

query = input("Enter your query\n")

IGNORED_DIR = Path(__file__).parent / "samples"
ROCKYOU_FILENAME = IGNORED_DIR / "rockyou.txt"
GENERATED_REPLY_FILE = IGNORED_DIR / f"{query}.txt"

amount_lines: int = 0
names_list = []


def find_lines(filename: Path, word_comb: str) -> Generator:
    with open(filename, "r") as file:
        while True:
            line = file.readline().replace("\n", "")
            if not line:
                break
            if word_comb in line.lower():
                yield line


def generate_file(filename: Path, word: str) -> None:
    with open(filename, "a") as file:
        file.write(f"{word}\n")


def file_info():
    print(f'Our search found {amount_lines} lines with query"{query}"')
    print(f"file size is {asizeof.asizeof(GENERATED_REPLY_FILE)}")


for line in find_lines(ROCKYOU_FILENAME, query):
    names_list.append(line)
    generate_file(GENERATED_REPLY_FILE, line)
    amount_lines += 1

file_info()
