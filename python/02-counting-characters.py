import tkinter as tk


EMPTY_MESSAGE = "The input is empty."


def command_line_main():
    try:
        while True:
            string = input("What is the input string? ")
            if not string:
                print("You have to enter something!")
                continue
            print(f"{string} has {len(string)} characters.")
    except (EOFError, KeyboardInterrupt):
        pass  # User has quit


def update_readout(input_field, output_field, event):
    print(event, input_field.get())
    input_string = input_field.get()
    print([input_field.get() for _ in range(10)])
    if not input_string:
        output_field["text"] = EMPTY_MESSAGE
    else:
        output_field["text"] = f"{input_string} has {len(input_string)} characters"


def main():
    root = tk.Tk()
    message = tk.Message(master=root, text="Enter a string:", width=400)
    message.pack(padx=20, pady=10, fill="both")

    text_field = tk.Entry(master=root, text="")
    text_field.pack(padx=20, pady=10, fill="both")

    readout = tk.Message(master=root, text=EMPTY_MESSAGE, width=400)
    readout.pack(padx=20, pady=10, fill="both")

    text_field.bind(
        "<KeyPress>",
        lambda ev: update_readout(
            input_field=text_field, output_field=readout, event=ev
        ),
    )

    root.mainloop()


if __name__ == "__main__":
    main()
