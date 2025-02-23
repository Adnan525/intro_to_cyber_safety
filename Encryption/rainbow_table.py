# =============================================================================
# What is a Rainbow Table?

# Think of a rainbow table like a giant cheat sheet or dictionary that contains:
# - Common passwords
# - Their pre-calculated hash values
# - Algorithms like MD5, SHA1 are quick to compute
# - MD5 is considered cryptographically broken due to collisions
# - NOTE: https://en.wikipedia.org/wiki/Collision_attack
# - Common passwords: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
# =============================================================================

import hashlib
from prettytable import PrettyTable
from pathlib import Path

def load_passwords_from_file(file_path):
    """
    Loads passwords from a text file where each password is on a new line
    
    Args:
        file_path (str): Path to the password file
        
    Returns:
        list: List of passwords, or default list if file not found
    """
    try:
        with open(file_path, 'r') as file:
            # Strip whitespace and filter out empty lines
            passwords = [line.strip() for line in file if line.strip()]
        return passwords
    except FileNotFoundError:
        print(f"Warning: Password file {file_path} not found. Using default passwords.")
        return [
            "password123",
            "qwerty",
            "admin123",
            "letmein",
            "welcome",
            "123456"
        ]


def create_rainbow_table(passwords):
    """
    Creates a rainbow table from a list of passwords
    
    Args:
        passwords (list): List of passwords to hash
        
    Returns:
        dict: Dictionary mapping hash values to passwords
    """
    rainbow_table = {}
    for password in passwords:
        hash_value = hashlib.md5(str(password).encode()).hexdigest()
        rainbow_table[hash_value] = password
    
    return rainbow_table


def display_rainbow_table(rainbow_table):
    """
    Displays the rainbow table in a formatted table
    
    Args:
        rainbow_table (dict): Dictionary of hash-password pairs
    """
    table = PrettyTable()
    table.field_names = ["Password", "MD5 Hash"]
    
    for hash_value, password in rainbow_table.items():
        table.add_row([password, hash_value])
    
    print("\nOur Rainbow Table:")
    print(table)


def check_stolen_password(rainbow_table):
    """
    Simulates checking a stolen password against the rainbow table
    
    Args:
        rainbow_table (dict): Dictionary of hash-password pairs
    """
    stolen_password = input("Enter a stolen password: ")
    stolen_hash = hashlib.md5(stolen_password.encode()).hexdigest()
    print(f"We found this hash in a database: {stolen_hash}")
    
    print("\nLooking up the hash in our rainbow table...")
    if stolen_hash in rainbow_table:
        found_password = rainbow_table[stolen_hash]
        print(f"Password found! It was: {found_password}")
    else:
        print("Password not found in rainbow table.")


def demonstrate_rainbow_table_attack(password_file="common_passwords.txt"):
    """
    Demonstrates how a rainbow table attack works
    
    Args:
        password_file (str, optional): Path to file containing passwords
    """
    print("=== Rainbow Table Demonstration ===")
    print("\nStep 1: Creating rainbow table from password list...")
    
    # Load passwords either from file or use defaults
    passwords = load_passwords_from_file(password_file)
    
    # Create and display the rainbow table
    rainbow_table = create_rainbow_table(passwords)
    display_rainbow_table(rainbow_table)
    
    print("\nStep 2: Simulating a data breach...")
    check_stolen_password(rainbow_table)
    

if __name__ == "__main__":
    """
    Example passwords.txt format:
    password123
    qwerty
    admin123
    letmein
    welcome
    123456
    """
    
    demonstrate_rainbow_table_attack()
