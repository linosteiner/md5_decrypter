import hashlib
import itertools
import string
import asyncio

class AsyncMD5Cracker:
    def __init__(self, target_hash: str, length: int, case: str):
        self.target_hash = target_hash
        self.length = length
        self.characters = self.get_character_set(case)

    def get_character_set(self, case: str):
        if case == "lower":
            return string.ascii_lowercase
        return string.ascii_letters  # Both lowercase and uppercase

    async def calculate_md5(self, text: str):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    async def generate_permutations(self):
        for perm in itertools.product(self.characters, repeat=self.length):
            yield ''.join(perm)
            await asyncio.sleep(0)

    async def crack(self):
        async for candidate in self.generate_permutations():
            hashed_candidate = await self.calculate_md5(candidate)
            if hashed_candidate == self.target_hash:
                print(f"Match found! {candidate} -> {hashed_candidate}")
                return candidate
        print("No match found.")
        return None

async def main():
    input_hash = input("Enter an MD5 hash to decrypt: ").strip()
    input_length = int(input("Enter the string length to decrypt: ").strip())
    input_case = input("Is the string lowercase (\"lower\") or both cases (\"both\")? ").strip()

    cracker = AsyncMD5Cracker(input_hash, input_length, input_case)
    result = await cracker.crack()

    if result:
        print(f"Decryption successful: {result}")
    else:
        print("Decryption failed.")

if __name__ == "__main__":
    asyncio.run(main())
