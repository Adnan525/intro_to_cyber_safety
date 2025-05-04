# =====================================================================================================
# D. He, Z. Liu, S. Zhu, S. Chan and M. Guizani, "Special Characters Usage and Its Effect on Password 
# Security," in IEEE Internet of Things Journal, 
# vol. 11, no. 11, pp. 19440-19453, 1 June1, 2024, doi: 10.1109/JIOT.2024.3367323.
# =====================================================================================================

import hashlib
import time
import argparse
import yaml
# from getpass import getpass
import threading
import queue
import os

def banner() -> None:
    """
    Display program banner and disclaimer
    """
    print("=" * 60)
    print("       PASSWORD DICTIONARY ATTACK DEMONSTRATION")
    print("              Created by Muntasir Adnan")
    print("=" * 60)
    print("WARNING: This tool is for EDUCATIONAL PURPOSES ONLY.")
    print("Using this tool against systems without explicit permission")
    print("is illegal and unethical.")
    print("=" * 60)
    print()
    
def print_enabled(to_print:str):
    print(f"{'\033[32m'}[✔] {to_print}{'\033[0m'}")
    

def load_substitutions(config_file: str = 'substitutions.yaml') -> dict:
    """
    Load character substitutions from YAML file
    
    Args:
        config_file (str): Path to the YAML configuration file
    """
    try:
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)
    except (FileNotFoundError, yaml.YAMLError):
        # Fallback
        print(f"Warning: Could not load {config_file}. Using default substitutions.")
        return {
            'a': ['@', '4'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['$', '5'],
            't': ['7'],
            'l': ['1'],
            'b': ['8'],
            'g': ['9'],
            'z': ['2']
        }


def load_special_symbols(symbols_file: str = 'special_symbols.txt') -> list:
    """
    Load special symbols from text file
    
    Args:
        symbols_file (str): Path to the special symbols file
    """
    try:
        with open(symbols_file, 'r') as file:
            symbols = file.read().strip().split('\n')
            return [s.strip() for s in symbols if s.strip()]
    except FileNotFoundError:
        return ['.', '!', '@', '-', '*', '?', '$', '#', '+', '/', '\\', '&', "'", '%']


def contains_symbol(password: str, symbols: list) -> bool:
    """
    Check if password already contains any special symbols
    
    Args:
        password (str): Password to check
        symbols (list): List of special symbols
    """
    return any(symbol in password for symbol in symbols)


def create_substitutions(password: str, 
                         substitution_map: dict, 
                         use_substitutions: bool = False) -> list:
    """
    Apply character substitutions to a password.
    Will apply one character at a time and generate all possible combinations.
    # TODO: Use full permutations for more complex substitutions, e.g. p@$sword vs p@s$word
    
    Args:
        password (str): Original password
        substitution_map (dict): Dictionary of substitutions
        use_substitutions (bool): Flag to enable/disable substitutions
    """
    if not use_substitutions:
        return [password]
    
    # Start with the original password
    result = [password]
    
    # Apply substitutions one character at a time
    for char, replacements in substitution_map.items():
        if char in password.lower():
            new_passwords = []
            for current_pass in result:
                # Keep original
                new_passwords.append(current_pass)
                
                # Add substituted versions
                for replacement in replacements:
                    # Replace all occurrences of the character (both upper and lower case)
                    new_pass = current_pass.replace(char, replacement)
                    new_pass = new_pass.replace(char.upper(), replacement)
                    new_passwords.append(new_pass)
            
            # Update our working set with the new passwords
            result = new_passwords
    
    # Remove duplicates
    return list(set(result))


def append_symbols(password: str, 
                   symbols: list, 
                   only_if_no_symbols: bool = False) -> list:
    """
    Append special symbols at the end to a password
    
    Args:
        password (str): Original password
        symbols (list): List of special symbols
        only_if_no_symbols (bool): Flag to append only if no symbols are present
    """
    result = [password]
    
    # Skip if we should only add symbols to passwords without symbols
    # and the password already contains symbols
    if only_if_no_symbols and contains_symbol(password, symbols):
        return result
    
    # Append each symbol to the password
    for symbol in symbols:
        # Modular approach: add symbol at the end
        # TODO: Add symbols at different positions if needed
        new_pass = password + symbol
        result.append(new_pass)
    
    return result


def worker(password_queue: queue.Queue, 
           result_queue: queue.Queue, 
           target_hash: str, 
           symbols: list, 
           substitution_map: dict, 
           use_substitutions: bool, 
           append_symbol: bool, 
           only_append_if_no_symbols: bool, 
           verbose: bool) -> None:
    """
    Worker thread for password cracking
    
    Args:
        password_queue (queue.Queue): Queue of passwords to process
        result_queue (queue.Queue): Queue for results
        target_hash (str): Target hash to crack
        symbols (list): List of special symbols
        substitution_map (dict): Dictionary of substitutions
        use_substitutions (bool): Flag to enable/disable substitutions
        append_symbol (bool): Flag to append symbols
        only_append_if_no_symbols (bool): Flag to append only if no symbols are present
        verbose (bool): Flag for verbose output
    """
    attempts = 0
    
    while True:
        try:
            # Get the next password from the queue
            base_password = password_queue.get_nowait()
        except queue.Empty:
            # No more passwords to process
            break
        
        # Generate variations with substitutions if enabled
        passwords_to_try = [base_password]
        
        if use_substitutions:
            passwords_to_try = create_substitutions(base_password, substitution_map, use_substitutions)
        
        # For each substitution variant, potentially append symbols
        all_variants = []
        for variant in passwords_to_try:
            if append_symbol or only_append_if_no_symbols:
                symbol_variants = append_symbols(variant, symbols, only_append_if_no_symbols)
                all_variants.extend(symbol_variants)
            else:
                all_variants.append(variant)
        
        # Now try all the password variants
        for test_password in all_variants:
            attempts += 1
            
            if verbose:
                print(f"Thread-{threading.current_thread().name} testing: {test_password}")
            
            test_hash = hashlib.sha256(test_password.encode()).hexdigest()
            
            if test_hash == target_hash:
                # Found the password!
                result_queue.put((True, test_password, base_password, attempts))
                return
        
        # Signal that we've processed this password
        password_queue.task_done()
    
    # Return the number of attempts made by this worker
    result_queue.put((False, None, None, attempts))


def demonstrate_password_cracking(use_substitutions=False, verbose=False, 
                                 config_file='substitutions.yaml', 
                                 append_symbol=False, only_append_if_no_symbols=False,
                                 num_threads=4):
    """Demonstrate dictionary-based password cracking with advanced options"""
    # The weak password we're demonstrating with
    weak_password = input("Enter a password: ")
    
    # Create SHA256 hash of the password
    password_hash = hashlib.sha256(weak_password.encode()).hexdigest()
    print(f"\nSHA256 hash of the password:")
    print(password_hash)
    print(f"Attempting to crack {password_hash}")
    
    # Load common passwords
    with open("common_passwords.txt", "r") as f:
        common_passwords = f.readlines()
        common_passwords = [p.strip() for p in common_passwords]
    
    print(f"Loaded {len(common_passwords)} common passwords from dictionary")
    
    # Load substitutions from YAML if enabled
    substitution_map = {}
    if use_substitutions:
        substitution_map = load_substitutions(config_file)
        print_enabled("Character substitution mode is ENABLED")
        print(f"Loaded {sum(len(v) for v in substitution_map.values())} possible character substitutions")
    
    # Load special symbols
    special_symbols = load_special_symbols() \
                      if append_symbol or only_append_if_no_symbols \
                      else []
    
    if append_symbol:
        print_enabled("Symbol appending is ENABLED")
    
    if only_append_if_no_symbols:
        print_enabled("Will only append symbols to passwords without existing symbols")
    
    if special_symbols is not []:
        print(f"Loaded {len(special_symbols)} special symbols for testing")
    
    # Threads
    print(f"Using {num_threads} threads for parallel processing")
    print("Starting cracking attempt...")
    
    # Setup for multithreading
    password_queue = queue.Queue()
    result_queue = queue.Queue()
    
    # Put all passwords in the queue
    for pwd in common_passwords:
        password_queue.put(pwd)
    
    # Start the timer
    start_time = time.time()
    
    # Create and start worker threads
    threads = []
    for i in range(num_threads):
        t = threading.Thread(
            target=worker,
            args=(password_queue, result_queue, password_hash, special_symbols,
                  substitution_map, use_substitutions, append_symbol, 
                  only_append_if_no_symbols, verbose),
            name=f"{i+1}"
        )
        t.daemon = True
        threads.append(t)
        t.start()
    
    # Wait for all passwords to be processed or a result to be found
    # Update progress periodically
    total_attempts = 0
    found = False
    
    while any(t.is_alive() for t in threads) and not found:
        try:
            # Check if any thread found the password
            result = result_queue.get(timeout=0.1)
            success, cracked_password, base_password, attempts = result
            
            if success:
                found = True
                end_time = time.time()
                print(f"\n[!] PASSWORD CRACKED!")
                print(f"[+] The password is: {cracked_password}")
                print(f"[+] Base dictionary word: {base_password}")
                print(f"[+] Time taken: {end_time - start_time:.2f} seconds")
                break
            else:
                total_attempts += attempts
                if verbose:
                    print(f"Thread completed, tested {attempts} passwords")
        except queue.Empty:
            # No results yet, continue waiting
            pass
        
        remaining = password_queue.qsize()
        if not verbose and remaining % 100 == 0:
            print(f"Passwords remaining: {remaining}")
    
    # Collect final attempt counts
    while not result_queue.empty():
        success, _, _, attempts = result_queue.get()
        if not success:  # Only count failed attempts
            total_attempts += attempts
    
    if not found:
        end_time = time.time()
        print("\nPassword NOT found in dictionary, even with advanced techniques"
              "(make sure it's enabled, use --help for more details).")
        print(f"Your password was: {weak_password}")
        print(f"Total passwords tested: {total_attempts}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")

# ===============================================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password Security Demonstration")
    parser.add_argument("-s", "--substitutions", action="store_true", 
                        help="Enable character substitutions")
    parser.add_argument("-a", "--append", action="store_true",
                        help="Append special symbols to passwords")
    parser.add_argument("-n", "--no-symbols", action="store_true",
                        help="Only append symbols to passwords without existing symbols")
    parser.add_argument("-v", "--verbose", action="store_true", 
                        help="Display each password being tested")
    parser.add_argument("-c", "--config", default="substitutions.yaml",
                        help="Path to substitutions YAML configuration file")
    parser.add_argument("-t", "--threads", type=int, default=4,
                        help="Number of threads to use (default: 4)")
    args = parser.parse_args()
    
    banner()
    
    demonstrate_password_cracking(
        use_substitutions=args.substitutions,
        verbose=args.verbose,
        config_file=args.config,
        append_symbol=args.append,
        only_append_if_no_symbols=args.no_symbols,
        num_threads=args.threads
    )