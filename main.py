def greet(name):
    name = name.strip()
    return f"Welcome, {name}!"


def main():
    print(greet(" Ram "))


if __name__ == "__main__":
    main()