def main():
    try:
        while True:
            string = input("What is the input string? ")
            if not string:
                print("You have to enter something!")
                continue
            print(f"{string} has {len(string)} characters.")
    except (EOFError, KeyboardInterrupt):
        pass    # User has quit


if __name__ == '__main__':
    main()
