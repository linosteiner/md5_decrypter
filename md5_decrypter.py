import hashlib
import itertools
import string
import time


class MD5Cracker:
    def __init__(self, target_hash: str, length: int, case: str):
        self.target_hash = target_hash
        self.length = length
        self.characters = self.get_character_set(case)

    def get_character_set(self, case: str):
        if case == "lower":
            return string.ascii_lowercase
        return string.ascii_letters  # Both lowercase and uppercase

    def calculate_md5(self, text: str):
        return hashlib.md5(text.encode("utf-8")).hexdigest()

    def crack(self):
        for candidate in itertools.product(self.characters, repeat=self.length):
            candidate_str = "".join(candidate)
            if self.calculate_md5(candidate_str) == self.target_hash:
                print(f"Match found! {candidate_str} -> {self.target_hash}")
                return candidate_str
        print("No match found.")
        return None


def main():
    input_hash = input("Enter an MD5 hash to decrypt: ").strip()
    input_length = int(input("Enter the string length to decrypt: ").strip())
    input_case = input('Is the string lowercase ("lower") or both cases ("both")? ').strip()

    start = time.time()
    cracker = MD5Cracker(input_hash, input_length, input_case)
    result = cracker.crack()
    end = time.time()

    print(f"Time taken to run the code was {end - start} seconds")

    if result:
        print(f"Decryption successful: {result}")
    else:
        print("Decryption failed.")


if __name__ == "__main__":
    main()