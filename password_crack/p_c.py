import hashlib
import time

def demonstrate_password_cracking():
    # The weak password we're demonstrating with
    weak_password = input("Enter a weak password: ")
    
    # Create SHA256 hash of the password
    password_hash = hashlib.sha256(weak_password.encode()).hexdigest()
    print(f"\nSHA256 hash of the password:")
    print(password_hash)
    print(f"Attempting to crack {password_hash}")
    print("Trying common passwords from a dictionary...")
    
    # List of common passwords to demonstrate dictionary attack
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.readlines()
        common_passwords = [p.replace("\n", "") for p in common_passwords]
    # Simulate cracking attempt
    start_time = time.time()
    
    for test_password in common_passwords:
        # print(f"\nTesting password: {test_password}")
        test_hash = hashlib.sha256(test_password.encode()).hexdigest()
        
        if test_hash == password_hash:
            end_time = time.time()
            print(f"\n[!] Password cracked!")
            print(f"[+] The password is: {test_password}")
            print(f"[+] Time taken: {end_time - start_time:.2f} seconds")
            return
        
        # Add a small delay to make the demonstration more visible
        time.sleep(0.5)
    
    print("\nPassword not found in dictionary.")

if __name__ == "__main__":
    print("=== Password Security Demonstration ===")
    print("This demo shows how weak passwords can be cracked")
    print("even when hashed with SHA256\n")
    
    demonstrate_password_cracking()
