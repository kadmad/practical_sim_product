import base64
from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Load the secret key securely
SECRET_KEY = b"OBHvJYuqLQRoAyvURxL4drcIQUZxz76D-upS6CLmWuQ="
cipher_suite = Fernet(SECRET_KEY)


def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data.decode()


def decrypt_data(encrypted_data):
    print("encrypted_data: ", encrypted_data, type(encrypted_data))
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
        print("decrypted_data: ", decrypted_data)
    except:
        decrypted_data = encrypted_data
    return decrypted_data
