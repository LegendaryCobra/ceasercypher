def password_encoder(password: str) -> str:
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def password_decoder(encoded_password: str) -> str:
    password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        password += decoded_digit
    return password


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = password_encoder(password)
        print("Your password has been encoded and stored!\n")
    elif choice == "2":
        encoded_password = input("Please enter your encoded password to decode: ")
        password = password_decoder(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {password}.\n")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.\n")
        