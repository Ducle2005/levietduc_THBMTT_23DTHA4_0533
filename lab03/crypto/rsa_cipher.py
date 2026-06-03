from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_rsa_keys():
    """
    Generate RSA 2048-bit key pair.
    Returns:
        tuple: (private_key_pem, public_key_pem) as strings.
    """
    key = RSA.generate(2048)
    private_key_pem = key.export_key().decode('utf-8')
    public_key_pem = key.publickey().export_key().decode('utf-8')
    return private_key_pem, public_key_pem

def rsa_encrypt(plaintext: str, public_key_pem: str) -> str:
    """
    Encrypt plaintext using the RSA public key (PKCS1_OAEP).
    Args:
        plaintext (str): The text to encrypt.
        public_key_pem (str): RSA public key in PEM format.
    Returns:
        str: Ciphertext in Base64 encoded format.
    """
    try:
        recipient_key = RSA.import_key(public_key_pem)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        ciphertext = cipher_rsa.encrypt(plaintext.encode('utf-8'))
        return base64.b64encode(ciphertext).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Mã hóa thất bại: {str(e)}")

def rsa_decrypt(ciphertext_b64: str, private_key_pem: str) -> str:
    """
    Decrypt Base64 ciphertext using the RSA private key (PKCS1_OAEP).
    Args:
        ciphertext_b64 (str): Base64 encoded ciphertext.
        private_key_pem (str): RSA private key in PEM format.
    Returns:
        str: Decrypted plaintext.
    """
    try:
        private_key = RSA.import_key(private_key_pem)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        ciphertext = base64.b64decode(ciphertext_b64.encode('utf-8'))
        decrypted = cipher_rsa.decrypt(ciphertext)
        return decrypted.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Giải mã thất bại. Vui lòng kiểm tra lại khóa hoặc bản mã: {str(e)}")
