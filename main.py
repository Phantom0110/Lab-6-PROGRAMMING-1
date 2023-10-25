def encoder(password):

    new_pass = ""

    for i in password:
        value = int(i)
        value += 3
        new_pass += str(value)

    return new_pass
def decode (encoded):
    string = ""
    value = 0
    for i in range(0, len(encoded)):
        value = int(encoded[i]) - 3
        string += str(value)
    return string

def main():

    encoded_password = None

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        menu_selection = int(input("Please enter an option: "))

        if menu_selection == 1:
            pass_input = input("Please enter your password to encode: ")
            encoded_password = encoder(pass_input)
            print("Your password has been encoded and stored!")

        if menu_selection == 2:
            decoded_password = decode(encoded_password)
            print("The encoded password is " + encoded_password + " ,and the original password is " + decoded_password + ".")

        if menu_selection == 3:
            break

if __name__ == "__main__":

    main()