x = True
encode = []
encoded_stng = ''
while x == True:
    print('Menu\n-------------\n 1. Encode\n2. Decode\n3. Quit\n')
    option = int(input('Please enter an option: '))
    if option == 1:
        encode = []
        value = input('Please enter your password to encode: ')
        for i in value:
            encode.append(str(int(i) + 3))
        encoded_stng = ''.join(encode)
        print('Your password has been encoded and stored!')
        print(encoded_stng)

    elif option == 2:
        decode = 0  # change the 0 later pls
        print(f"The encoded password is {decode}, and the original password is {encoded_stng}.")
    elif option == 3:
        x = False
        break
