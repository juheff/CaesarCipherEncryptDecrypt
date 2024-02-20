def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            # Shift the character by the specified amount
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
        
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Shift the character back by the specified amount
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            
            decrypted_text += char
    return decrypted_text

def main():
    # Get user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
