x = True
encoded_stng = ''

def encode(password):
    encode = []
    for i in password:
        i = int(i)
        if i >= 7:
            encode.append(str(int(i) - 7))
        else:
            encode.append(str(int(i) + 3))

    return ''.join(encode)


def decode(original):
    decode = []
    res = [int(ele) for ele in original]
    for i in res:
        if i == 0:
            decode.append(7)
        if i == 1:
            decode.append(8)
        if i == 2:
            decode.append(9)
        if i == 3:
            decode.append((0))
        if i > 3:
            decode.append((int(i)-3))
    return decode



name = 0
value = 0
while x == True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
    option = int(input('Please enter an option: '))
    if option == 1:
        value = input('Please enter your password to encode: ')
        print('Your password has been encoded and stored!')
        name = (encode(value))

    elif option == 2:
        value2 = decode(name)
        print(f"The encoded password is {name}, and the original password is {value}.")
    elif option == 3:
        x = False
        break
