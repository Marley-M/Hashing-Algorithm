# Imports hashing library
import hashlib

# A list of available hash formats
hash_format_available = ["sha224", "sha256", "sha384", "sha512", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "blake2b", "blake2s", "sha1", "md5"]

# Defines the hashing code to be called later
def hash_format_choose_def():
    # Ask user what hash format to use
    # Adds answer to variable "hash_format"
    hash_format = input("""What hash format do you want to use.
Type "list" for a list of all hashing formats available.
    > """)
    if hash_format in hash_format_available: # Checks if requested hash format is usable
        while True:
            # Creates a new hash object using the chosen hash format
            if hash_format == "sha224":
                hash_object = hashlib.sha224()
            elif hash_format == "sha256":
                hash_object = hashlib.sha256()
            elif hash_format == "sha384":
                hash_object = hashlib.sha384()
            elif hash_format == "sha512":
                hash_object = hashlib.sha512()
            elif hash_format == "sha3_224":
                hash_object = hashlib.sha3_224()
            elif hash_format == "sha3_256":
                hash_object = hashlib.sha3_256()
            elif hash_format == "sha3_384":
                hash_object = hashlib.sha3_384()
            elif hash_format == "sha3_512":
                hash_object = hashlib.sha3_512()
            elif hash_format == "blake2b":
                hash_object = hashlib.blake2b()
            elif hash_format == "blake2s":
                hash_object = hashlib.blake2s()
            elif hash_format == "sha1":
                hash_object = hashlib.sha1()
            elif hash_format == "md5":
                hash_object = hashlib.md5()

            # Update the hash object with the bytes of the string
            hash_object.update(data.encode())

            # Get the hexadecimal representation of the hash
            hex_dig = hash_object.hexdigest()

            # Prints the hashed data
            print(hex_dig)

            break

    if hash_format == "list": # If user imputs "list" when asked for a hashing format it prints a list of all usable hashing formats
        print("""        - sha224
        - sha256
        - sha384
        - sha512
        - sha3_224
        - sha3_256
        - sha3_384
        - sha3_512
        - blake2b
        - blake2s
        - sha1
        - md5
""")
        # Calls defined code for hashing
        hash_format_choose_def()

    elif hash_format not in "list": # If user inputs a hash format that isn't recognised it asks them to try again.
        print("""That is not a usable hash format, please select again.
              """)
        
        # Calls defined code for hashing
        hash_format_choose_def()

while True:
    # Asks user for something to hash
    # Adds answer to variable "data"
    data = input("""
What do you want to hash?
    > """)

    # Calls defined code for hashing
    hash_format_choose_def()