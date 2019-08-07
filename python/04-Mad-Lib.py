# Mad Libs are really tedious, so I’m not doing the
# challenges for this one.
def main():
    try:
        while True:
            noun = input("Enter a noun: ")
            verb = input("Enter a verb: ")
            adjective = input("Enter an adjective: ")
            adverb = input("Enter an adverb: ")
            print(
                f"Do you {verb} your {adjective} {noun} {adverb}? "
                "That’s hilarious!"
            )
    except (KeyboardInterrupt, EOFError):
        print()

if __name__ == '__main__':
    main()
