import hashlib
import itertools
import string
import os

# Function to hash passwords using different algorithms
def hash_password(password, algorithm):
    try:
        if algorithm == 'md5':
            return hashlib.md5(password.encode()).hexdigest()
        elif algorithm == 'sha1':
            return hashlib.sha1(password.encode()).hexdigest()
        elif algorithm == 'sha224':
            return hashlib.sha224(password.encode()).hexdigest()
        elif algorithm == 'sha256':
            return hashlib.sha256(password.encode()).hexdigest()
        elif algorithm == 'sha384':
            return hashlib.sha384(password.encode()).hexdigest()
        elif algorithm == 'sha512':
            return hashlib.sha512(password.encode()).hexdigest()
        elif algorithm == 'sha3_224':
            return hashlib.sha3_224(password.encode()).hexdigest()
        elif algorithm == 'sha3_256':
            return hashlib.sha3_256(password.encode()).hexdigest()
        elif algorithm == 'sha3_384':
            return hashlib.sha3_384(password.encode()).hexdigest()
        elif algorithm == 'sha3_512':
            return hashlib.sha3_512(password.encode()).hexdigest()
        elif algorithm == 'shake_128':
            return hashlib.shake_128(password.encode()).hexdigest(32)  # Adjust length as needed
        elif algorithm == 'shake_256':
            return hashlib.shake_256(password.encode()).hexdigest(64)  # Adjust length as needed
        elif algorithm == 'blake2b':
            return hashlib.blake2b(password.encode()).hexdigest()
        elif algorithm == 'blake2s':
            return hashlib.blake2s(password.encode()).hexdigest()
        else:
            raise ValueError("Unsupported hash algorithm")
    except Exception as e:
        return str(e)

# Function to create a dictionary file with common passwords
def create_dictionary_file(filename):
    passwords = [
        "password", "123456", "123456789", "qwerty", "abc123", "letmein", "welcome",
        "admin", "password1", "1234567", "monkey", "sunshine", "12345678", "12345",
        "iloveyou", "princess", "1234567", "admin123", "password123", "qwerty123"
    ]
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(f"{password}\n")

# Function to crack passwords using a dictionary attack
def crack_password_from_dict(hash_to_crack, dictionary_file, algorithm):
    try:
        with open(dictionary_file, 'r') as file:
            for line in file:
                password = line.strip()
                hashed_password = hash_password(password, algorithm)
                if hashed_password == hash_to_crack:
                    return password
    except FileNotFoundError:
        return "Dictionary file not found."

    return "Password not found."

# Function to generate all combinations of passwords up to a given length
def brute_force_crack(hash_to_crack, max_length, algorithm):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            if hash_password(password, algorithm) == hash_to_crack:
                return password
    return "Password not found."

def main():
    hash_to_crack = input("Enter the hash to crack: ").strip()
    algorithm = input("Enter the hash algorithm (e.g., md5, sha256, etc.): ").strip()
    dictionary_file = 'dictionary.txt'

    create_dictionary_file(dictionary_file)

    # Attempt to crack using dictionary attack
    password = crack_password_from_dict(hash_to_crack, dictionary_file, algorithm)
    if password == "Password not found.":
        # If dictionary attack fails, attempt brute-force cracking
        max_length = int(input("Enter the maximum length for brute-force cracking: ").strip())
        password = brute_force_crack(hash_to_crack, max_length, algorithm)

    print(f"Cracked password: {password}")

if __name__ == "__main__":
    main()
