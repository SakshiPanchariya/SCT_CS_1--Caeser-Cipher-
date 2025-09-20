def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        elif char.isdigit():
            result +=chr((ord(char)-ord('0')+shift) % 10 + ord('0'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter your message:")
shift = int(input("Enter shift value:"))
choice = input("Encrypt or Decrypt?(E/D):").upper()
if choice == 'E':
    print("Encrypted message:", encrypt(message, shift))
elif choice == 'D':
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice!")




