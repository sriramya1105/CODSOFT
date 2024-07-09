import random
import string

def generate_password(length, complexity):
    # Generates a random password of the specified length and type of complexity.
    if complexity == 'simple':
        characters = string.ascii_letters + string.digits
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Choose 'simple' or 'strong'.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename="passwords.txt"):
    # Save the generated password to a file.
    with open(filename, "a") as file:
        file.write(password + "\n")

def password_generator():
    # Function to run the password generator.
    print("Welcome to CodSoft Password Generator!")
    
    try:
        length = int(input("Enter the preferred password length: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return

        complexity = input("Enter the password complexity (simple/strong): ").lower()
        password = generate_password(length, complexity)
        print("Generated password:", password)

        if input("Do you want to save this password? (yes/no): ").lower() == "yes":
            save_password(password)
            print("Password saved successfully!")

    except ValueError as e:
        print("Invalid input.", e)

# Call the function explicitly
password_generator()