import hashlib


def calculate_md5(text):
    md5_hash = hashlib.md5()

    encoded_text = text.encode('utf-8')

    md5_hash.update(encoded_text)

    return md5_hash.hexdigest()


def main():
    text = "aavc"
    md5_hash = calculate_md5(text)
    print(md5_hash)

if __name__ == "__main__":
    main()
