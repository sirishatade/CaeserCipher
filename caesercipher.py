alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caeser(text, type, shift):
    return_value = ""
    for i in text:
        index = alphabet.index(i)
        if type == "encode":
            return_value += alphabet[(index + shift) % 26]
        else:
            return_value += alphabet[(index - shift) % 26]
    return return_value


response = "yes"

while response == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(f"Here's the {direction}d result: {caeser(text, direction, shift)}")
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
