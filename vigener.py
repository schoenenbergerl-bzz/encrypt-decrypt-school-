alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def extend_key(text, key):
    key = key.upper()
    extended_key = []
    key_index = 0
    for i in range(len(text)):
        if text[i] != " ":
            extended_key.append(alphabet.index(key[key_index % len(key)]))
            key_index += 1
        else:
            extended_key.append(" ")
    return extended_key

def encode(text, key):
    coded_text = []
    text = text.upper()
    key_indices = extend_key(text, key)
    for i in range(len(text)):
        if text[i] != " ":
            text_index = alphabet.index(text[i])
            new_index = (text_index + key_indices[i]) % 26
            coded_text.append(alphabet[new_index])
        else:
            coded_text.append(" ")
    return "".join(coded_text)

def decode(text, key):
    decoded_text = []
    text = text.upper()
    key_indices = extend_key(text, key)
    for i in range(len(text)):
        if text[i] != " ":
            text_index = alphabet.index(text[i])
            new_index = (text_index - key_indices[i]) % 26
            decoded_text.append(alphabet[new_index])
        else:
            decoded_text.append(" ")
    return "".join(decoded_text)

if __name__ == '__main__':
    operation = int(input("encode(1) or decode(2): "))

    if operation == 1:
        text = input("Text: ")
        key = input("Key: ")
        print(encode(text, key))
    elif operation == 2:
        text = input("Text: ")
        key = input("Key: ")
        print(decode(text, key))
