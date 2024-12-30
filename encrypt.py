class CustomCipher:
    def __init__(self):  
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.substitution_key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    def substitution_encrypt(self, message):
        message = message.upper()
        return ''.join(self.substitution_key[self.alphabet.index(c)] if c in self.alphabet else c for c in message)

    def substitution_decrypt(self, encrypted_message):
        return ''.join(self.alphabet[self.substitution_key.index(c)] if c in self.substitution_key else c for c in encrypted_message)

    def matrix_encrypt(self, message):
        message = message.upper().replace(" ", "")
        while len(message) % 3 != 0:
            message += 'X'

        key = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        numeric_message = [self.alphabet.index(c) for c in message]
        encrypted_message = ""

        for i in range(0, len(numeric_message), 3):
            row = numeric_message[i:i+3]
            for col in range(3):
                
                value = sum(row[row_idx] * key[row_idx][col] for row_idx in range(3)) % 26
                encrypted_message += self.alphabet[value]

        return encrypted_message

cipher = CustomCipher()
message = "HELLO WORLD"
encrypted_message = cipher.substitution_encrypt(message)
decrypted_message = cipher.substitution_decrypt(encrypted_message)

print(f"Original: {message}")
print(f"Encrypted (Substitution): {encrypted_message}")
print(f"Decrypted (Substitution): {decrypted_message}")

matrix_encrypted_message = cipher.matrix_encrypt(message)
print(f"Encrypted (Matrix): {matrix_encrypted_message}")
