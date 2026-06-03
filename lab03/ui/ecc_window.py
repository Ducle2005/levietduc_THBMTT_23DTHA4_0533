from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt
from crypto.ecc_signature import generate_ecc_keys, ecc_sign, ecc_verify

class ECCWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ECC Digital Signature")
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
        title_label = QLabel("ECC P-256 Digital Signature (ECDSA)")
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
        self.btn_gen_key = QPushButton("Generate ECC Key")
        self.btn_gen_key.setCursor(Qt.PointingHandCursor)
        self.btn_gen_key.setStyleSheet("padding: 10px; font-size: 14px;")
        self.btn_gen_key.clicked.connect(self.handle_generate_key)
        main_layout.addWidget(self.btn_gen_key)
        
        # Message input
        main_layout.addWidget(QLabel("Message (Thông điệp):"))
        self.message_txt = QTextEdit()
        self.message_txt.setPlaceholderText("Nhập nội dung cần ký...")
        self.message_txt.setMaximumHeight(100)
        main_layout.addWidget(self.message_txt)
        
        # Sign/Verify controls layout
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(20)
        
        # Left side: Sign
        sign_layout = QVBoxLayout()
        self.btn_sign = QPushButton("Sign Message (Ký chữ ký)")
        self.btn_sign.setCursor(Qt.PointingHandCursor)
        self.btn_sign.clicked.connect(self.handle_sign)
        sign_layout.addWidget(self.btn_sign)
        
        # Right side: Verify
        verify_layout = QVBoxLayout()
        self.btn_verify = QPushButton("Verify Signature (Xác minh)")
        self.btn_verify.setCursor(Qt.PointingHandCursor)
        self.btn_verify.clicked.connect(self.handle_verify)
        verify_layout.addWidget(self.btn_verify)
        
        actions_layout.addLayout(sign_layout)
        actions_layout.addLayout(verify_layout)
        main_layout.addLayout(actions_layout)
        
        # Signature output
        main_layout.addWidget(QLabel("Signature (Base64) (Chữ ký):"))
        self.signature_txt = QTextEdit()
        self.signature_txt.setPlaceholderText("Chữ ký số dạng Base64...")
        self.signature_txt.setMaximumHeight(80)
        main_layout.addWidget(self.signature_txt)
        
        # Verification status output
        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("Kết quả xác minh (Verification Result):"))
        self.status_val = QLineEdit()
        self.status_val.setReadOnly(True)
        self.status_val.setStyleSheet("font-weight: bold; font-size: 14px; text-align: center; padding: 5px;")
        self.status_val.setPlaceholderText("Chưa thực hiện xác minh")
        status_layout.addWidget(self.status_val)
        main_layout.addLayout(status_layout)
        
        # Back Button
        self.btn_back = QPushButton("Quay lại Menu")
        self.btn_back.setStyleSheet("background-color: #4f545c; font-weight: normal; margin-top: 10px;")
        self.btn_back.clicked.connect(self.close)
        main_layout.addWidget(self.btn_back)

    def handle_generate_key(self):
        try:
            self.private_key, self.public_key = generate_ecc_keys()
            self.pub_key_txt.setPlainText(self.public_key)
            self.priv_key_txt.setPlainText(self.private_key)
            QMessageBox.information(self, "Thành công", "Sinh cặp khóa ECC P-256 thành công!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể sinh cặp khóa: {str(e)}")

    def handle_sign(self):
        if not self.private_key:
            QMessageBox.warning(self, "Lỗi", "Vui lòng sinh khóa ECC trước khi thực hiện ký!")
            return
            
        message = self.message_txt.toPlainText()
        if not message:
            QMessageBox.warning(self, "Thông báo", "Vui lòng nhập Message cần ký!")
            return
            
        try:
            signature = ecc_sign(message, self.private_key)
            self.signature_txt.setPlainText(signature)
            self.status_val.clear()
            self.status_val.setPlaceholderText("Chưa thực hiện xác minh")
            self.status_val.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; color: #b9bbbe; background-color: #2b2b36;")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi ký", str(e))

    def handle_verify(self):
        if not self.public_key:
            QMessageBox.warning(self, "Lỗi", "Vui lòng sinh khóa ECC trước khi xác minh chữ ký!")
            return
            
        message = self.message_txt.toPlainText()
        signature = self.signature_txt.toPlainText().strip()
        
        if not signature:
            QMessageBox.warning(self, "Thông báo", "Vui lòng có chữ ký (Signature) để xác minh!")
            return
            
        is_valid = ecc_verify(message, signature, self.public_key)
        
        if is_valid:
            self.status_val.setText("Chữ ký HỢP LỆ (Signature is Valid)")
            self.status_val.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; color: #43b581; background-color: #2b2b36; border: 1px solid #43b581;")
            QMessageBox.information(self, "Kết quả xác minh", "Chữ ký hợp lệ!")
        else:
            self.status_val.setText("Chữ ký KHÔNG HỢP LỆ (Signature is Invalid)")
            self.status_val.setStyleSheet("font-weight: bold; font-size: 14px; padding: 5px; color: #f04747; background-color: #2b2b36; border: 1px solid #f04747;")
            QMessageBox.warning(self, "Kết quả xác minh", "Chữ ký KHÔNG hợp lệ! Bản tin có thể đã bị sửa đổi hoặc chữ ký không đúng.")
