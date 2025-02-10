# =============================================================================================
# Message: "Hello, World!"
# MD5:    65a8e27d8879283831b664bd8b7f0ad4
# SHA1:   0a9f2a6772942557ab5355d76af442f8f65e824f
# SHA256: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
# MD5 decrypt: https://10015.io/tools/md5-encrypt-decrypt
# =============================================================================================
import hashlib

def demonstrate_hashing():
    """
    Demonstrates different hashing algorithms
    """
    print("\n=== Hashing Demo ===")
    
    # Original message
    message = "Hello, World!"
    print(f"Original message: {message}")
    
    # MD5 (Note: MD5 is considered cryptographically broken)
    md5_hash = hashlib.md5(message.encode()).hexdigest()
    print(f"\nMD5 hash: {md5_hash}")
    
    # SHA-256
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    print(f"\nSHA-256 hash: {sha256_hash}")
    
    # Demonstrate hash properties
    print("\nDemonstrating hash properties...")
    
    # 1. Same input = Same hash
    print("\n1. Same input produces same hash:")
    print(f"Hash of 'Hello, World!': {hashlib.sha256('Hello, World!'.encode()).hexdigest()}")
    print(f"Hash of 'Hello, World!': {hashlib.sha256('Hello, World!'.encode()).hexdigest()}")
    
    # 2. Different input = Completely different hash
    print("\n2. Small change produces completely different hash:")
    print(f"Hash of 'Hello, World!': {hashlib.sha256('Hello, World!'.encode()).hexdigest()}")
    print(f"Hash of 'Hello, World?': {hashlib.sha256('Hello, World?'.encode()).hexdigest()}")
