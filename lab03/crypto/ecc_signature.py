from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import base64

def generate_ecc_keys():
    """
    Generate ECC key pair using P-256 curve.
    Returns:
        tuple: (private_key_pem, public_key_pem) as strings.
    """
    key = ECC.generate(curve='P-256')
    private_key_pem = key.export_key(format='PEM')
    public_key_pem = key.public_key().export_key(format='PEM')
    return private_key_pem, public_key_pem

def ecc_sign(message: str, private_key_pem: str) -> str:
    """
    Sign a message using the ECC private key and SHA256 + DSS/ECDSA.
    Args:
        message (str): Message to sign.
        private_key_pem (str): ECC private key in PEM format.
    Returns:
        str: Signature in Base64 encoded format.
    """
    try:
        key = ECC.import_key(private_key_pem)
        h = SHA256.new(message.encode('utf-8'))
        signer = DSS.new(key, 'fips-186-3')
        signature = signer.sign(h)
        return base64.b64encode(signature).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Ký thông điệp thất bại: {str(e)}")

def ecc_verify(message: str, signature_b64: str, public_key_pem: str) -> bool:
    """
    Verify a signature using the ECC public key and SHA256 + DSS/ECDSA.
    Args:
        message (str): Original or modified message.
        signature_b64 (str): Base64 encoded signature.
        public_key_pem (str): ECC public key in PEM format.
    Returns:
        bool: True if signature is valid, False otherwise.
    """
    try:
        key = ECC.import_key(public_key_pem)
        h = SHA256.new(message.encode('utf-8'))
        verifier = DSS.new(key, 'fips-186-3')
        signature = base64.b64decode(signature_b64.encode('utf-8'))
        verifier.verify(h, signature)
        return True
    except (ValueError, TypeError, Exception):
        return False
