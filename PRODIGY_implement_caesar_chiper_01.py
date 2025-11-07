def caesar_cipher_encrypt(msg, num):
    result = ""
    for char in msg:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + num) % 26 + base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(msg, num):
    return caesar_cipher_encrypt(msg, -num)

# --- Main Program ---
print("====== Caesar Cipher Encryption =====")
message = input("Enter your message: ")
num = int(input("Enter Shift Number (e.g., 1): "))

encrypted = caesar_cipher_encrypt(message, num)
decrypted = caesar_cipher_decrypt(encrypted, num)

print("\n--- Results ---")
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")
