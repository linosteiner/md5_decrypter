import hashlib


def capture_input():
    input_string = input("Enter a string to decrypt: ")
    if not input_string.isalpha():
        print(f"\"{input_string}\" is not a valid string. Only uppercase and lowercase letters are allowed.")
        capture_input()
    else:
        return input_string


def calculate_md5(text):
    md5_hash = hashlib.md5()
    encoded_text = text.encode('utf-8')
    md5_hash.update(encoded_text)
    return md5_hash.hexdigest()


def main():
    text = "aavc"
    text = capture_input()
    md5_hash = calculate_md5(str(text))
    print(md5_hash)


if __name__ == "__main__":
    main()
    print("test")
