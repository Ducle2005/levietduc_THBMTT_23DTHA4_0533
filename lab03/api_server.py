import sys
import os
from flask import Flask, request, jsonify

# Ensure the lab03 folder is in path for modules import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crypto.rsa_cipher import generate_rsa_keys, rsa_encrypt, rsa_decrypt
from crypto.ecc_signature import generate_ecc_keys, ecc_sign, ecc_verify

app = Flask(__name__)

# Global variables to store keys in memory
rsa_private_key = None
rsa_public_key = None

ecc_private_key = None
ecc_public_key = None

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Lab03 RSA ECC API is running"
    })

@app.route('/rsa/generate-key', methods=['POST'])
def rsa_generate_key():
    global rsa_private_key, rsa_public_key
    try:
        rsa_private_key, rsa_public_key = generate_rsa_keys()
        return jsonify({
            "message": "RSA key generated successfully",
            "public_key": rsa_public_key,
            "private_key": rsa_private_key
        })
    except Exception as e:
        return jsonify({"error": f"Không thể tạo khóa RSA: {str(e)}"}), 400

@app.route('/rsa/encrypt', methods=['POST'])
def rsa_encrypt_endpoint():
    global rsa_public_key
    if not rsa_public_key:
        return jsonify({"error": "Khóa công khai RSA chưa được tạo. Vui lòng gọi /rsa/generate-key trước."}), 400
        
    data = request.get_json(silent=True)
    if not data or 'plaintext' not in data:
        return jsonify({"error": "Thiếu tham số bắt buộc 'plaintext' trong JSON body."}), 400
        
    plaintext = data['plaintext']
    try:
        ciphertext = rsa_encrypt(plaintext, rsa_public_key)
        return jsonify({
            "plaintext": plaintext,
            "ciphertext": ciphertext
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/rsa/decrypt', methods=['POST'])
def rsa_decrypt_endpoint():
    global rsa_private_key
    if not rsa_private_key:
        return jsonify({"error": "Khóa bí mật RSA chưa được tạo. Vui lòng gọi /rsa/generate-key trước."}), 400
        
    data = request.get_json(silent=True)
    if not data or 'ciphertext' not in data:
        return jsonify({"error": "Thiếu tham số bắt buộc 'ciphertext' trong JSON body."}), 400
        
    ciphertext = data['ciphertext']
    try:
        decrypted_text = rsa_decrypt(ciphertext, rsa_private_key)
        return jsonify({
            "decrypted_text": decrypted_text
        })
    except Exception as e:
        return jsonify({"error": f"Giải mã thất bại: {str(e)}"}), 400

@app.route('/ecc/generate-key', methods=['POST'])
def ecc_generate_key_endpoint():
    global ecc_private_key, ecc_public_key
    try:
        ecc_private_key, ecc_public_key = generate_ecc_keys()
        return jsonify({
            "message": "ECC key generated successfully",
            "public_key": ecc_public_key,
            "private_key": ecc_private_key
        })
    except Exception as e:
        return jsonify({"error": f"Không thể tạo khóa ECC: {str(e)}"}), 400

@app.route('/ecc/sign', methods=['POST'])
def ecc_sign_endpoint():
    global ecc_private_key
    if not ecc_private_key:
        return jsonify({"error": "Khóa bí mật ECC chưa được tạo. Vui lòng gọi /ecc/generate-key trước."}), 400
        
    data = request.get_json(silent=True)
    if not data or 'message' not in data:
        return jsonify({"error": "Thiếu tham số bắt buộc 'message' trong JSON body."}), 400
        
    message = data['message']
    try:
        signature = ecc_sign(message, ecc_private_key)
        return jsonify({
            "message": message,
            "signature": signature
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/ecc/verify', methods=['POST'])
def ecc_verify_endpoint():
    global ecc_public_key
    if not ecc_public_key:
        return jsonify({"error": "Khóa công khai ECC chưa được tạo. Vui lòng gọi /ecc/generate-key trước."}), 400
        
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Thiếu dữ liệu JSON body."}), 400
        
    if 'message' not in data:
        return jsonify({"error": "Thiếu tham số bắt buộc 'message' trong JSON body."}), 400
    if 'signature' not in data:
        return jsonify({"error": "Thiếu tham số bắt buộc 'signature' trong JSON body."}), 400
        
    message = data['message']
    signature = data['signature']
    
    try:
        is_valid = ecc_verify(message, signature, ecc_public_key)
        if is_valid:
            return jsonify({
                "valid": True,
                "message": "Signature is valid"
            })
        else:
            return jsonify({
                "valid": False,
                "message": "Signature is invalid"
            })
    except Exception as e:
        return jsonify({"error": f"Xác minh thất bại: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
