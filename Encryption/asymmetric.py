# ======================================================================================================
# NOTE: https://www.youtube.com/watch?v=4zahvcJ9glg
# RSA (Rivest-Shamir-Adleman)
# Example - ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA7gR7... user@hostname
# ======================================================================================================

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import base64

def demonstrate_asymmetric_encryption():
    """
    Demonstrates asymmetric encryption using RSA
    """
    print("\n=== Asymmetric Encryption Demo ===")
    
    # Generate key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    
    print(f"Generated private key: {private_key}")
    print("Successfully generated public key..")
    print()
    
    # Original message
    message = input("Enter a message to encrypt with RSA: ")
    print(f"Original message: {message}")
    
    # Encrypt message
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"\nEncrypted message (in base64): {base64.b64encode(encrypted).decode()}")
    
    # Decrypt message
    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"\nDecrypted message: {decrypted.decode()}")