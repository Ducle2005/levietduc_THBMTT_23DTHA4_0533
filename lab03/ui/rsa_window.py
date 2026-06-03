from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt
from crypto.rsa_cipher import generate_rsa_keys, rsa_encrypt, rsa_decrypt

class RSAWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RSA Encryption / Decryption")
        self.resize(800, 600)
        
        # Local keys storage
        self.private_key = None
        self.public_key = None
        
        self.init_ui()
        
    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Title Label
        title_label = QLabel("RSA 2048-bit Encryption & Decryption")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #5865f2; margin-bottom: 10px;")
        main_layout.addWidget(title_label)
        
        # Grid layout for keys
        keys_layout = QGridLayout()
        keys_layout.setSpacing(10)
        
        pub_label = QLabel("Public Key (PEM):")
        self.pub_key_txt = QTextEdit()
        self.pub_key_txt.setReadOnly(True)
        self.pub_key_txt.setPlaceholderText("Khóa công khai (Public Key) sẽ hiển thị ở đây...")
        self.pub_key_txt.setMaximumHeight(150)
        
        priv_label = QLabel("Private Key (PEM):")
        self.priv_key_txt = QTextEdit()
        self.priv_key_txt.setReadOnly(True)
        self.priv_key_txt.setPlaceholderText("Khóa bí mật (Private Key) sẽ hiển thị ở đây...")
        self.priv_key_txt.setMaximumHeight(150)
        
        keys_layout.addWidget(pub_label, 0, 0)
        keys_layout.addWidget(self.pub_key_txt, 1, 0)
        keys_layout.addWidget(priv_label, 0, 1)
        keys_layout.addWidget(self.priv_key_txt, 1, 1)
        
        main_layout.addLayout(keys_layout)
        
        # Button: Generate Key
        self.btn_gen_key = QPushButton("Generate RSA Key")
        self.btn_gen_key.setCursor(Qt.PointingHandCursor)
        self.btn_gen_key.setStyleSheet("padding: 10px; font-size: 14px;")
        self.btn_gen_key.clicked.connect(self.handle_generate_key)
        main_layout.addWidget(self.btn_gen_key)
        
        # Texts and actions layout
        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)
        
        # Left side: Plaintext & Encrypt
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Plaintext (Bản rõ):"))
        self.plaintext_txt = QTextEdit()
        self.plaintext_txt.setPlaceholderText("Nhập nội dung cần mã hóa...")
        left_layout.addWidget(self.plaintext_txt)
        
        self.btn_encrypt = QPushButton("Encrypt (Mã hóa)")
        self.btn_encrypt.setCursor(Qt.PointingHandCursor)
        self.btn_encrypt.clicked.connect(self.handle_encrypt)
        left_layout.addWidget(self.btn_encrypt)
        
        # Right side: Ciphertext & Decrypt & Decrypted Text
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Ciphertext (Base64) (Bản mã):"))
        self.ciphertext_txt = QTextEdit()
        self.ciphertext_txt.setPlaceholderText("Bản mã dạng Base64...")
        right_layout.addWidget(self.ciphertext_txt)
        
        self.btn_decrypt = QPushButton("Decrypt (Giải mã)")
        self.btn_decrypt.setCursor(Qt.PointingHandCursor)
        self.btn_decrypt.clicked.connect(self.handle_decrypt)
        right_layout.addWidget(self.btn_decrypt)
        
        right_layout.addWidget(QLabel("Decrypted Text (Bản giải mã):"))
        self.decrypted_txt = QTextEdit()
        self.decrypted_txt.setReadOnly(True)
        self.decrypted_txt.setPlaceholderText("Nội dung sau khi giải mã...")
        self.decrypted_txt.setMaximumHeight(100)
        right_layout.addWidget(self.decrypted_txt)
        
        content_layout.addLayout(left_layout)
        content_layout.addLayout(right_layout)
        
        main_layout.addLayout(content_layout)
        
        # Back Button
        self.btn_back = QPushButton("Quay lại Menu")
        self.btn_back.setStyleSheet("background-color: #4f545c; font-weight: normal; margin-top: 10px;")
        self.btn_back.clicked.connect(self.close)
        main_layout.addWidget(self.btn_back)

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
