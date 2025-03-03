import hashlib
import itertools
import re
import string
import time


def get_character_set(case):
    """
    Return a string of characters based on the given case.
    :param case: "lower" or "both"
    """
    if case == "lower":
        return string.ascii_lowercase
    return string.ascii_letters


def calculate_md5(text):
    """
    Return the MD5 hash of the input text.
    :param text: String to hash
    :return: A 32-character hexadecimal MD5 hash
    """
    return hashlib.md5(text.encode("utf-8")).hexdigest()


class MD5Cracker:
    def __init__(self, target_hash, length, case):
        """
        Initializes an MD5Cracker instance for brute-force decryption of an MD5 hash.

        Args:
            target_hash (str): The MD5 hash to be brute-forced.
            length (int): The length of the target string (number of characters).
            case (str): The character set specification:
                        - "lower": Uses lowercase English letters (a-z).
                        - "both": Uses both uppercase and lowercase letters (A-Z, a-z).

        Attributes:
            target_hash (str): Stores the target MD5 hash to be matched.
            length (int): Defines the length of the candidate strings to be generated.
            characters (str): The set of characters allowed in the candidate strings,
                              determined by the `case` parameter.
            total_attempts (int): The total number of possible candidate strings, calculated
                                  as `len(self.characters) ** self.length`, which provides an
                                  estimate of the brute-force complexity.
        """
        self.target_hash = target_hash
        self.length = length
        self.characters = get_character_set(case)
        self.total_attempts = len(self.characters) ** self.length

    def crack(self):
        """
        Brute-force the MD5 hash by iterating over all possible combinations.
        :return: The matching string if found, otherwise None
        """
        print(f"Total possible attempts: {self.total_attempts}")

        # Iterate over all possible combinations of characters of the given length
        for candidate in itertools.product(self.characters, repeat=self.length):
            # Convert the tuple of characters into a string
            candidate_str = "".join(candidate)
            if calculate_md5(candidate_str) == self.target_hash:
                print(f"Match found! {candidate_str} -> {self.target_hash}")
                return candidate_str
        print("No match found.")
        return None


def get_input_hash():
    while True:
        input_hash = input("Enter an MD5 hash to decrypt (32 hex chars): ").strip()
        if re.fullmatch(r"[a-fA-F0-9]{32}", input_hash):
            return input_hash
        print("Invalid MD5 hash. It must be exactly 32 hexadecimal characters.")


def get_length_str():
    while True:
        length_str = input("Enter the string length to decrypt (positive integer): ").strip()
        if length_str.isdigit():
            input_length = int(length_str)
            if 0 < input_length <= 8:
                return input_length
        print("Invalid length. Please enter a positive integer.")


def get_input_case():
    while True:
        input_case = input('Is the string lowercase ("lower") or both cases ("both")? ').strip().lower()
        if input_case in ("lower", "both"):
            return input_case
        print('Invalid input. Please enter "lower" or "both".')


def main():
    # Get the inputs for hash, length and case
    input_hash = get_input_hash()
    input_length = get_length_str()
    input_case = get_input_case()

    # Brute force a result with the MD5Cracker class
    start = time.time()
    cracker = MD5Cracker(input_hash, input_length, input_case)
    result = cracker.crack()
    end = time.time()

    print(f"Time taken to run the code: {end - start:.2f} seconds")

    if not result:
        print("Decryption failed.")


if __name__ == "__main__":
    main()
