text = input("Enter your text: ")
shift = int(input("Enter shift value: "))

encrypted = ""

# Encryption
for char in text:
    if char.isalpha():
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted += char

print("Encrypted Text:", encrypted)

decrypted = ""

# Decryption
for char in encrypted:
    if char.isalpha():
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted += char

print("Decrypted Text:", decrypted)