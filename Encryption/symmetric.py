# =======================================================================================================
# NOTE: https://cryptography.io/en/latest/fernet/
# Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.

# AES (Advanced Encryption Standard)
# Block Size: 128 bits
# Key Sizes: 128, 192, or 256 bits
# Used by: U.S. Government, WhatsApp, ZIP files

# DES (Data Encryption Standard)
# Block Size: 64 bits
# Key Size: 56 bits
# Status: Deprecated due to small key size
# =======================================================================================================

from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

def demonstrate_symmetric_encryption():
    """
    Demonstrates symmetric encryption using Fernet (AES)
    """
    print("\n=== Symmetric Encryption Demo ===")
    
    # Generate a key
    key = Fernet.generate_key()
    print(f"Generated fernet key: {key}")
    f = Fernet(key)
    
    # Original message
    message = input("Enter a message to encrypt with Fernet: ")
    print(f"Original message: {message}")
    
    # Encrypt the message
    encrypted_message = f.encrypt(message.encode())
    print(f"\nEncrypted message: {encrypted_message.decode()}")
    
    # Decrypt the message
    decrypted_message = f.decrypt(encrypted_message)
    print(f"\nDecrypted message: {decrypted_message.decode()}")
    
    # Demonstrate what happens with wrong key
    wrong_key = Fernet.generate_key()
    f_wrong = Fernet(wrong_key)
    print("\nTrying to decrypt with wrong key...")
    try:
        f_wrong.decrypt(encrypted_message)
    except InvalidToken as e:
        # raise e
        print("Decryption failed: Invalid token! The key does not match.")