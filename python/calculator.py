def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mult(x, y):
    return x*y


def div(x, y):
    return x/y


def mod(x, y):
    return x % y


def pow(x, y):
    return x**y


def main():
    x = int(input("First number:"))
    y = int(input("Second number:"))
    print(f"The sum of {x} and {y}:", add(x, y))
    print(f"The difference of {x} from {y}:", sub(x, y))
    print(f"The product of {x} and {y}:", mult(x, y))
    print(f"The division of {x} and {y}:", div(x, y))
    print(f"The modulos of {x} and {y}:", mod(x, y))
    print(f"{x} to the power of {y}:", pow(x, y))


if __name__ == "__main__":
    main()
