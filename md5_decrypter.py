import hashlib
import itertools
import multiprocessing
import string
import time


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

    def crack(self):
        num_workers = multiprocessing.cpu_count()
        queue = multiprocessing.Queue()
        processes = []

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

        print("No match found.")
        return None


def main():
    input_hash = input("Enter an MD5 hash to decrypt: ").strip()
    input_length = int(input("Enter the string length to decrypt: ").strip())
    input_case = input("Is the string lowercase (\"lower\") or both cases (\"both\")? ").strip()

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
