def decode_phone_number(encoded_number):
    # Mengambil dua digit terakhir setelah karakter '-'
    decoded_number = encoded_number.split('-')[-1]
    return decoded_number

# Contoh penggunaan
encoded_number = "••••-••••-••14"
decoded_number = decode_phone_number(encoded_number)
print(decoded_number)  # Output: 14
