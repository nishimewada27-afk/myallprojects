from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher = Fernet(key)

print("Encryption key:", key.decode())

# Encrypt
msg = input("Enter a message: ").encode()
encrypted_msg = cipher.encrypt(msg)
print("Encrypted:", encrypted_msg)

# Decrypt
decrypted_msg = cipher.decrypt(encrypted_msg).decode()
print("Decrypted:", decrypted_msg)
