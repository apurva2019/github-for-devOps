"""
Program: User Greeting and Age Validator
Description: This program takes user input, validates age,
and prints a friendly message.
Author: Apurva
"""


def is_adult(age: int) -> bool:
    """
    Check if the given age qualifies as an adult.

    Args:
        age (int): Age of the user

    Returns:
        bool: True if age >= 18, else False
    """
    return age >= 18


def greet_user(name: str, age: int) -> None:
    """
    Greet the user based on their age.

    Args:
        name (str): Name of the user
        age (int): Age of the user
    """
    if is_adult(age):
        print(f"Hello {name}, you are an adult.")
    else:
        print(f"Hello {name}, you are a minor.")


def main() -> None:
    """
    Main function to execute the program.
    """
    name: str = input("Enter your name: ")
    age: int = int(input("Enter your age: "))

    greet_user(name, age)


if __name__ == "__main__":
    main()
