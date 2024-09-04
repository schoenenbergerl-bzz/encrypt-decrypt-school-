alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def encode(text, key):
    key = key % 26
    coded_text = ""
    text = text.upper()
    text_list = list(text)
    for x in text_list:
        if x == " ":
            text_list.remove(x)
    for letter in text_list:
        index = alphabet.index(letter)
        if key + index > 25:
            index -= 26
        coded_text += alphabet[index + key]
    return coded_text

def decode(text, key):
    key = key % 26
    decoded_text = ""
    text = text.upper()
    text_list = list(text)
    for x in text_list:
        if x == " ":
            text_list.remove(x)
    for letter in text_list:
        index = alphabet.index(letter)
        if key + index < 0:
            index += 26
        decoded_text += alphabet[index - key]
    return decoded_text

if __name__ == '__main__':
    operation = int(input("encode(1) or decode(2): "))

    if operation == 1:
        text = input("Text: ")
        key = int(input("Key: "))
        print(encode(text, key))
    elif operation == 2:
        text = input("Text: ")
        key = int(input("Key: "))
        print(decode(text, key))
