
import random
import string


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    # Define character sets based on user preferences
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        return "Error: No character set selected. Please choose at least one option."

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user input for password complexity
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
    print(f"Your generated password is: {password}")

main()
