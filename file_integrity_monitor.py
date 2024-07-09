import hashlib
import os

def calculate_hash(file_path):
    """Calculate the SHA-256 hash of the file."""
    try:
        with open(file_path, 'rb') as file:
            file_hash = hashlib.sha256()
            chunk = file.read(4096)
            while chunk:
                file_hash.update(chunk)
                chunk = file.read(4096)
            return file_hash.hexdigest()
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None

def modify_file(file_path):
    """Modify the file to simulate a change."""
    try:
        with open(file_path, 'a') as file:
            file.write("debug_mode: enabled\n")
        print(f"File '{file_path}' has been modified to simulate tampering.")
    except FileNotFoundError:
        print("File not found during modification. Please check the path and try again.")

def check_file_integrity(original_hash, file_path):
    """Check if the file has been altered by comparing hashes."""
    new_hash = calculate_hash(file_path)
    if new_hash != original_hash:
        print("File integrity compromised! The file has been altered.")
    else:
        print("File integrity is intact.")

def main():
    file_path = 'config.txt'
    print("Select an option:")
    print("2: Calculate Original Hash")
    print("3: Modify File")
    print("4: Check File Integrity")

    choice = input("Enter your choice (2-4): ")
    if choice == '2':
        hash_value = calculate_hash(file_path)
        if hash_value:
            print(f"Original hash of the file: {hash_value}")
            # Save the hash for later verification
            with open("hash_store.txt", 'w') as hash_file:
                hash_file.write(hash_value)
        else:
            print("Error calculating the hash.")
    elif choice == '3':
        modify_file(file_path)
    elif choice == '4':
        try:
            with open("hash_store.txt", 'r') as hash_file:
                original_hash = hash_file.read().strip()
            check_file_integrity(original_hash, file_path)
        except FileNotFoundError:
            print("Hash file not found. Please run step 2 first to calculate and store the hash.")

if __name__ == "__main__":
    main()
