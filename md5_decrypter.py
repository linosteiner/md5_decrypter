import hashlib
import itertools
import multiprocessing
import re
import string
import time

MAX_ALLOWED_STRING_LENGTH = 8


def calculate_md5(text: str):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def worker(target_hash, characters, length, queue):
    for candidate in itertools.product(characters, repeat=length):
        candidate_str = "".join(candidate)
        if calculate_md5(candidate_str) == target_hash:
            queue.put(candidate_str)
            return


def get_character_set(case: str):
    return string.ascii_lowercase if case == "lower" else string.ascii_letters


class MD5Cracker:
    def __init__(self, target_hash: str, length: int, case: str):
        self.target_hash = target_hash
        self.length = length
        self.characters = get_character_set(case)
        self.total_attempts = len(self.characters) ** self.length

    def crack(self):
        num_workers = multiprocessing.cpu_count()
        queue = multiprocessing.Queue()
        processes = []

        print(f"Total possible attempts: {self.total_attempts}")

        for _ in range(num_workers):
            p = multiprocessing.Process(target=worker, args=(self.target_hash, self.characters, self.length, queue))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        if not queue.empty():
            match = queue.get()
            print(f"Match found! {match} -> {self.target_hash}")
            return match

        print("No match found after exhaustive search.")
        return None


def is_valid_md5(hash_str):
    """ Validate if the input is a valid 32-character hexadecimal MD5 hash. """
    return bool(re.fullmatch(r"[a-fA-F0-9]{32}", hash_str))


def main():
    while True:
        input_hash = input("Enter an MD5 hash to decrypt: ").strip()
        if is_valid_md5(input_hash):
            break
        else:
            print("Error: Invalid MD5 hash. It must be a 32-character hexadecimal string.")

    while True:
        try:
            input_length = int(
                input(f"Enter the string length to decrypt (maximum {MAX_ALLOWED_STRING_LENGTH} characters): ").strip())
            if 1 <= input_length <= MAX_ALLOWED_STRING_LENGTH:
                break
            else:
                print(f"Error: Length must be between 1 and {MAX_ALLOWED_STRING_LENGTH}.")
        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        input_case = input("Is the string lowercase (\"lower\") or both cases (\"both\")? ").strip()
        if input_case in {"lower", "both"}:
            break
        else:
            print('Error: Input must be either "lower" or "both".')

    start = time.time()
    cracker = MD5Cracker(input_hash, input_length, input_case)

    result = cracker.crack()
    end = time.time()

    print(f"Time taken: {end - start:.2f} seconds")

    if result:
        print(f"Decryption successful: {result}")
    else:
        print("Decryption failed.")


if __name__ == "__main__":
    main()
