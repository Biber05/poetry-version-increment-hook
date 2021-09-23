from dataclasses import dataclass


@dataclass
class Version:
    major: int
    minor: int
    patch: int

    def inc_major(self):
        self.major += 1
        return self.__str__()

    def inc_minor(self):
        self.minor += 1
        return self.__str__()

    def inc_patch(self):
        self.patch += 1
        return self.__str__()

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"
