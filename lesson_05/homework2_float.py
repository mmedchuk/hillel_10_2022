class Frange:
    def __init__(self, start, stop=None, step=1):
        self.step = step
        if stop is None:
            self.start = 0
            self.stop = start

        else:
            self.start, self.stop = start, stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.stop:
                raise StopIteration
        else:
            if self.start <= self.stop:
                raise StopIteration
        char = self.start
        self.start += self.step
        return char


assert list(Frange(5)) == [0, 1, 2, 3, 4]
assert list(Frange(2, 5)) == [2, 3, 4]
assert list(Frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(Frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(Frange(1, 5)) == [1, 2, 3, 4]
assert list(Frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(Frange(0, 0)) == []
assert list(Frange(100, 0)) == []

print("SUCCESS!")
