def min(f: int, v : int) -> int:
    if (f < v):
        return f
    else:
        return v


def print_min(f: int, v: int) -> None:
    if (f < v):
        print(f)
    else:
        print(v)


number1: int = int(input("3"))
number2: int = int(input("6"))
print(min(3, 6))