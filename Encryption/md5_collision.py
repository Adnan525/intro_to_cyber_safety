# =====================================================================================================
# NOTE: https://crypto.stackexchange.com/questions/1434/are-there-two-known-strings-which-have-the-same-md5-hash-value
# =====================================================================================================

import hashlib
import binascii

def demonstrate_md5_collision():
    """
    Demonstrates a real MD5 collision using a known example
    """
    print("=== MD5 Collision Demonstration ===")
    
    # Two different hex strings that produce the same MD5 hash
    # 555 and d55
    # 200a and 202a
    hex_string1 = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"
    hex_string2 = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"
    
    # Convert hex strings to binary
    binary1 = binascii.unhexlify(hex_string1)
    binary2 = binascii.unhexlify(hex_string2)
    
    # Calculate MD5 hashes of the binary data
    md5_1 = hashlib.md5(binary1).hexdigest()
    md5_2 = hashlib.md5(binary2).hexdigest()
    
    # Calculate SHA256 hashes to show they're different
    sha256_1 = hashlib.sha256(binary1).hexdigest()
    sha256_2 = hashlib.sha256(binary2).hexdigest()
    
    print("\nHex String 1:", hex_string1)
    print("Hex String 2:", hex_string2)
    
    # print("\nDifferences in hex strings:")
    # # Find and show the positions where strings differ
    # differences = [(i, c1, c2) for i, (c1, c2) in enumerate(zip(hex_string1, hex_string2)) if c1 != c2]
    # for pos, char1, char2 in differences:
    #     print(f"Position {pos}: '{char1}' vs '{char2}'")
    
    print("\nMD5 hashes:")
    print("Binary 1 MD5:", md5_1)
    print("Binary 2 MD5:", md5_2)
    print("\nSHA256 hashes (notice these are different):")
    print("Binary 1 SHA256:", sha256_1)
    print("Binary 2 SHA256:", sha256_2)
    
    print("\nResults:")
    print(f"Binary data is identical? {'Yes' if binary1 == binary2 else 'No'}")
    print(f"MD5 hashes match? {'Yes' if md5_1 == md5_2 else 'No'}")
    print(f"SHA256 hashes match? {'Yes' if sha256_1 == sha256_2 else 'No'}")

if __name__ == "__main__":
    demonstrate_md5_collision()