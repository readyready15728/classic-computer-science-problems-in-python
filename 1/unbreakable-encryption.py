from secrets import token_bytes

def random_key(length):
    tb = token_bytes(length)
    return int.from_bytes(tb, 'big')

def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, 'big')
    encrypted = original_key ^ dummy
    return dummy, encrypted

def decrypt(message, key):
    # Because XOR is commutative, "message" and "key" are arbitrary but make
    # for readability IMO

    # The arithmetic below prevents off-by-one errors
    decrypted = message ^ key
    decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return decrypted_bytes.decode()

message, key = encrypt('One time pad!')
print(decrypt(message, key))
