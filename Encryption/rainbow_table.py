# =============================================================================
# What is a Rainbow Table?

# Think of a rainbow table like a giant cheat sheet or dictionary that contains:
# - Common passwords
# - Their pre-calculated hash values
# - Algorithms like MD5, SHA1 are quick to compute
# - MD5 is considered cryptographically broken due to collisions
#   NOTE: https://en.wikipedia.org/wiki/Collision_attack
# =============================================================================

import hashlib
from prettytable import PrettyTable

def create_mini_rainbow_table():
    """
    Creates a small rainbow table to demonstrate the concept
    """
    # Common passwords people might use
    common_passwords = [
        "password123",
        "qwerty",
        "admin123",
        "letmein",
        "welcome",
        "123456"
    ]
    
    # Create our "rainbow table"
    rainbow_table = {}
    for password in common_passwords:
        hash_value = hashlib.md5(password.encode()).hexdigest()
        rainbow_table[hash_value] = password
    
    return rainbow_table

def demonstrate_rainbow_table_attack():
    """
    Demonstrates how a rainbow table attack works
    """
    print("=== Rainbow Table Demonstration ===")
    print("\nStep 1: Creating a small rainbow table of common passwords...")
    rainbow_table = create_mini_rainbow_table()
    
    # Create a pretty table for display
    table = PrettyTable()
    table.field_names = ["Password", "MD5 Hash"]
    
    for hash_value, password in rainbow_table.items():
        table.add_row([password, hash_value])
    
    print("\nOur Mini Rainbow Table:")
    print(table)
    
    print("\nStep 2: Let's simulate a data breach...")
    # Simulate a "stolen" password hash
    stolen_password = input("Enter a stolen password: ")
    stolen_hash = hashlib.md5(stolen_password.encode()).hexdigest()
    print(f"We found this hash in a database: {stolen_hash}")
    
    print("\nStep 3: Looking up the hash in our rainbow table...")
    if stolen_hash in rainbow_table:
        found_password = rainbow_table[stolen_hash]
        print(f"Password found! It was: {found_password}")
    else:
        print("Password not found in rainbow table.")
    
    # print("\nThis is why we need:")
    # print("1. Strong passwords (not common ones)")
    # print("2. Salt values (makes rainbow tables useless)")
    # print("3. Better hashing algorithms (like SHA256 + salt)")

if __name__ == "__main__":
    demonstrate_rainbow_table_attack()