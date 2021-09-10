import timeit


def encrypt(message: str, key: int):
    encrypted_message = ""
    for i in range(key):
        j = 0
        while i + j < len(message):
            encrypted_message += message[i + j]
            j += key
    return encrypted_message


def decrypt(message: str, key: int):
    decrypted_message = list(message)
    k = 0
    for i in range(key):
        j = 0
        while i + j < len(message):
            decrypted_message[i + j] = message[k]
            k += 1
            j += key
    return ''.join(decrypted_message)


if __name__ == '__main__':
    with open('text.txt', 'r+') as f:
        text = f.read()
    encryption_time = timeit.timeit("""
encrypted = encrypt(text, 8)
with open('encrypted.txt', 'r+') as f:
    f.seek(0)
    f.write(text)
    f.truncate()""", globals=globals(), number=1)
    with open('encrypted.txt', 'r+') as f:
        encrypted = f.read()
    decryption_time = timeit.timeit("""
decrypted = decrypt(encrypted, 8)
with open('decrypted.txt', 'r+') as f:
    f.seek(0)
    f.write(text)
    f.truncate()""", globals=globals(), number=1)
    print(f'Encryption time is:  {encryption_time}')
    print(f'Decryption time is:  {decryption_time}')
