def encrypt(message, shiftnumber):
    # Encrypt while preserving case and special characters
    encrypted = ''
    for c in message:
        if c.isalpha():
            # Handle letters while preserving case
            ascii_offset = ord('A') if c.isupper() else ord('a') 
            encrypted += chr((ord(c) - ascii_offset + shiftnumber) % 26 + ascii_offset)
        else:
            # Keep special characters and numbers unchanged
            encrypted += c
    return encrypted

def decrypt(message, shiftnumber): 
    # Decrypt while preserving case and special characters
    # Reuse encrypt function with negative shift
    return encrypt(message, -shiftnumber)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e','d']:
            print("Invalid choice. Please enter 'e' or 'd'")
            continue
            
        message = input("Enter the message: ")
        try:
            shiftnumber = int(input("Enter the shift number: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 'e':
            result = encrypt(message, shiftnumber)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shiftnumber)
            print(f"Decrypted message: {result}")

        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break
        
if __name__ == '__main__':
    main()
