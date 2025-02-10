import hashlib
import time

def demonstrate_hash_comparison():
    """
    Demonstrates the difference between MD5 and SHA256 encryption
    """
    # Common passwords to demonstrate
    test_passwords = [
        "password123",
        "qwerty",
        "admin123",
        "letmein",
        "welcome"
    ]
    
    print("=== MD5 vs SHA256 Security Demonstration ===")
    
    for password in test_passwords:
        print(f"\nHashing common passwords: {password}")
        
        # Generate both hashes
        md5_hash = hashlib.md5(password.encode()).hexdigest()
        sha256_hash = hashlib.sha256(password.encode()).hexdigest()
        
        print(f"\nMD5 hash:    {md5_hash}")
        print(f"SHA256 hash: {sha256_hash}")
        time.sleep(1)  # Pause for readability
            
    print("\nWhy is SHA256 more secure?")
    print("1. Longer hash length (256 bits vs 128 bits)")
    print("2. No known collisions (unlike MD5)")
    print("3. Would require massive rainbow tables")