from symmetric import demonstrate_symmetric_encryption
from asymmetric import demonstrate_asymmetric_encryption
from hashing import demonstrate_hashing
from rainbow_table import demonstrate_rainbow_table_attack
from sha256_vs_md5 import demonstrate_hash_comparison
from md5_collision import demonstrate_md5_collision

def demo(selection: int) -> None:
    if selection == 1:
        demonstrate_symmetric_encryption()
    elif selection == 2:
        demonstrate_asymmetric_encryption()
    elif selection == 3:
        demonstrate_hashing()
    elif selection == 4:
        demonstrate_rainbow_table_attack()
    elif selection == 5:
        demonstrate_hash_comparison()
    elif selection == 6:
        demonstrate_md5_collision()
    else:
        print("Invalid selection. Please try again.")


def main():
    while True:
        print("=== Encryption and Hashing Demos ===")
        print("1. Symmetric Encryption (AES)")
        print("2. Asymmetric Encryption (RSA)")
        print("3. Hashing Algorithms (MD5, SHA256)")
        print("4. Rainbow Table Attack")
        print("5. MD5 vs SHA256 Security")
        print("6. MD5 Collision Demonstration")
        print("0. Exit")
        selection = int(input("Enter the number of the demo you'd like to run: "))
        if selection == 0:
            break
        demo(selection)
        print("="*50)

if __name__ == "__main__":
    main()
    