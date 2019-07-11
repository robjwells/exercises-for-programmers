SEEN = set()


def get_greeting(name):
    if name in SEEN:
        return f'Welcome back, {name}.'
    SEEN.add(name)
    return f'Hello, {name}, nice to meet you!'
    

def ask_for_name():
    return input('What is your name? ')


def greet(name):
    print(get_greeting(name))


if __name__ == '__main__':
    while True:
        greet(ask_for_name())

