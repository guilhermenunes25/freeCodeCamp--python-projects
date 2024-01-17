text = 'Hello Zaira'
custom_key = 'python'

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
         #Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
             #Find the right key character to encode    
            key_char = key[key_index % len(key)]
            key_index += 1
            index = alphabet.find(char)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

