from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher


app = Flask(__name__)
caesar_cipher = CaesarCipher()


@app.route("/", methods=["GET"])
def index():
    return "Caesar Cipher API is running"


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json

    if data is None or "plain_text" not in data or "key" not in data:
        return jsonify({"error": "Missing plain_text or key"}), 400

    plain_text = data["plain_text"]

    try:
        key = int(data["key"])
    except (ValueError, TypeError):
        return jsonify({"error": "Key must be an integer"}), 400

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json

    if data is None or "cipher_text" not in data or "key" not in data:
        return jsonify({"error": "Missing cipher_text or key"}), 400

    cipher_text = data["cipher_text"]

    try:
        key = int(data["key"])
    except (ValueError, TypeError):
        return jsonify({"error": "Key must be an integer"}), 400

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
