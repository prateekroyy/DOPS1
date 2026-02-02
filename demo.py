def greet(name):
    return f"Hello, {name}! Welcome to Git branching 🚀"


def main():
    user = input("Enter your name: ")
    message = greet(user)
    print(message)


if __name__ == "__main__":
    main()
