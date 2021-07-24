import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print (art.logo)

crypting = True

def cipher(text, shift):
    cryptedText = ""
    if direction == "decode":
        shift *= -1
    for i in range(0, len(text)):
        if text[i] in alphabet:
            num = alphabet.index(text[i]) + shift
            if num > len(alphabet) - 1:
                num = (num - len(alphabet))
            cryptedText += alphabet[num]
        else:
            cryptedText += text[i]
    if direction == "encode":
        print(f"The encoded text is {cryptedText}")
    elif direction == "decode":
        print(f"The decoded text is {cryptedText}")
    else:
        print ("Try Again")

while crypting:
    ask = input("Do you want to cipher a phrase? ")
    if ask == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > len(alphabet):
            shift %= 26
        cipher(text, shift)
    else:
        print ("Have a nice day.")
        crypting = False


