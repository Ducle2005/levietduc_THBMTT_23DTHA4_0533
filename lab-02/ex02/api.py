from flask import Flask, request, jsonify
from cipher.vigenere import VigenereCipher


app = Flask(__name__)
vigenere_cipher = VigenereCipher()


@app.route("/", methods=["GET"])
def index():
    return "Vigenere API is running"


@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt_api():
    data = request.json

    if data is None or "plain_text" not in data or "key" not in data:
        return jsonify({"error": "Missing plain_text or key"}), 400

    plain_text = data["plain_text"]
    key = data["key"]

    if not isinstance(key, str) or key == "":
        return jsonify({"error": "Key must not be empty"}), 400

    if not key.isalpha():
        return jsonify({"error": "Key must contain only letters"}), 400

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt_api():
    data = request.json

    if data is None or "cipher_text" not in data or "key" not in data:
        return jsonify({"error": "Missing cipher_text or key"}), 400

    cipher_text = data["cipher_text"]
    key = data["key"]

    if not isinstance(key, str) or key == "":
        return jsonify({"error": "Key must not be empty"}), 400

    if not key.isalpha():
        return jsonify({"error": "Key must contain only letters"}), 400

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
