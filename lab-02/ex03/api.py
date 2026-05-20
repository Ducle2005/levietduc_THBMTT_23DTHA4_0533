from flask import Flask, request, jsonify
from cipher.railfence import RailFenceCipher


app = Flask(__name__)
railfence_cipher = RailFenceCipher()


@app.route("/", methods=["GET"])
def index():
    return "Rail Fence API is running"


@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json

    if data is None or "plain_text" not in data or "key" not in data:
        return jsonify({"error": "Missing plain_text or key"}), 400

    plain_text = data["plain_text"]

    try:
        key = int(data["key"])
    except (ValueError, TypeError):
        return jsonify({"error": "Key must be an integer"}), 400

    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json

    if data is None or "cipher_text" not in data or "key" not in data:
        return jsonify({"error": "Missing cipher_text or key"}), 400

    cipher_text = data["cipher_text"]

    try:
        key = int(data["key"])
    except (ValueError, TypeError):
        return jsonify({"error": "Key must be an integer"}), 400

    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
