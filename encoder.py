passencode = {'0': '3', '1': '4', '2': '5', '3': '6',
              '4': '7', '5': '8', '6': '9', '7': '0',
              '8': '1', '9': '2'}

passdecode = {'0': '7', '1': '8', '2': '9', '3': '0',
              '4': '1', '5': '2', '6': '3', '7': '4',
              '8': '5', '9': '6'}


def encode(code):
    y = list(code)
    x = ''
    for digit in y:
        x += passencode[digit]
    return x


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        user_input = int(input("Please enter an option: "))

        if user_input == 1:
            encode_input = input("Please enter your password to encode: ")
            encoded_password = encode(encode_input)
            print(f"Your password has been encoded and stored! {encoded_password} \n")
