import hashlib
import itertools
import string


def calculate_md5(text):
    md5_hash = hashlib.md5()
    encoded_text = text.encode('utf-8')
    md5_hash.update(encoded_text)
    return md5_hash.hexdigest()


def decrypt(input_hash, input_length, input_case):
    iterate_through_alphabet(input_case)
    return True


def iterate_through_alphabet(case):
    if case == "lower":
        for char in itertools.chain(string.ascii_lowercase):
            print(char)
    else:
        for char in itertools.chain(string.ascii_lowercase, string.ascii_uppercase):
            print(char)


def main():
    input_hash = input("Enter an MD5 hash to decrypt: ")
    input_length = input("Enter a string length to decrypt: ")
    input_case = input("Is the string upper (\"lower\") or upper- and lowercase (\"both\")? ")
    decrypt(input_hash, input_length, input_case)


if __name__ == "__main__":
    main()
