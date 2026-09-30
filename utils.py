def print_header(title):
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def get_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid number.")


def pause():
    input("\nPress Enter to continue...")
