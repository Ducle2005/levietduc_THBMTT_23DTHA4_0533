import os
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from crypto.rsa_cipher import generate_rsa_keys, rsa_encrypt, rsa_decrypt

class RSAWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Load the UI file dynamically
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rsa.ui')
        uic.loadUi(ui_path, self)
        
        # Local keys storage
        self.private_key = None
        self.public_key = None
        
        self.init_connections()
        
    def init_connections(self):
        # Connect buttons defined in rsa.ui to handler methods
        self.btn_gen_key.clicked.connect(self.handle_generate_key)
        self.btn_encrypt.clicked.connect(self.handle_encrypt)
        self.btn_decrypt.clicked.connect(self.handle_decrypt)
        self.btn_back.clicked.connect(self.close)

    def handle_generate_key(self):
        try:
            self.private_key, self.public_key = generate_rsa_keys()
            self.pub_key_txt.setPlainText(self.public_key)
            self.priv_key_txt.setPlainText(self.private_key)
            QMessageBox.information(self, "Thành công", "Sinh cặp khóa RSA 2048-bit thành công!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể sinh cặp khóa: {str(e)}")

    def handle_encrypt(self):
        if not self.public_key:
            QMessageBox.warning(self, "Lỗi", "Vui lòng sinh khóa RSA trước khi thực hiện mã hóa!")
            return
            
        plaintext = self.plaintext_txt.toPlainText()
        if not plaintext:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập Plaintext cần mã hóa!")
            return
            
        try:
            ciphertext = rsa_encrypt(plaintext, self.public_key)
            self.ciphertext_txt.setPlainText(ciphertext)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi mã hóa", str(e))

    def handle_decrypt(self):
        if not self.private_key:
            QMessageBox.warning(self, "Lỗi", "Vui lòng sinh khóa RSA trước khi thực hiện giải mã!")
            return
            
        ciphertext = self.ciphertext_txt.toPlainText().strip()
        if not ciphertext:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập Ciphertext cần giải mã!")
            return
            
        try:
            decrypted = rsa_decrypt(ciphertext, self.private_key)
            self.decrypted_txt.setPlainText(decrypted)
        except Exception as e:
            self.decrypted_txt.setPlainText("Lỗi giải mã")
            QMessageBox.warning(self, "Lỗi giải mã", "Giải mã không thành công! Bản mã đã bị thay đổi hoặc khóa không khớp.")
