def prompt_for_quote():
    return input("What is the quote? ")


def prompt_for_person():
    return input("Who said it? ")


def main():
    person_quote_pairs = []
    while True:
        try:
            quote = prompt_for_quote()
            if not quote:
                break
            person = prompt_for_person()
            person_quote_pairs.append((person, quote))
        except (KeyboardInterrupt, EOFError):
            break
    for person, quote in person_quote_pairs:
        print(person + ' says, "' + quote + '"')


if __name__ == "__main__":
    main()
