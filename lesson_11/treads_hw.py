from math import ceil
from threading import Thread
from typing import Generator

PRIMES_LIST: list = []


def get_ranges(start: int, end: int, amount: int) -> Generator:
    part_len: int = ceil(len(range(start, end)) / amount)

    for i in range(start, end, part_len):
        if i + part_len > end:
            yield i, end
        else:
            yield i, i + part_len


def get_primes_list(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    for i in results:
        PRIMES_LIST.append(i)


def get_primes(start: int, end: int, amount_of_threads: int) -> list[int]:

    ranges = get_ranges(start, end, amount_of_threads)

    threads = []

    for i in range(amount_of_threads):
        start_range, end_range = next(ranges)
        thread = Thread(target=get_primes_list, args=(start_range, end_range))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(PRIMES_LIST)


get_primes(10, 1000, 10)
