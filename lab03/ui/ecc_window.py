import os
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import uic
from crypto.ecc_signature import generate_ecc_keys, ecc_sign, ecc_verify

class ECCWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Load the UI file dynamically
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ecc.ui')
        uic.loadUi(ui_path, self)
        
        # Local keys storage
        self.private_key = None
        self.public_key = None
        
        self.init_connections()
        
    def init_connections(self):
        # Connect buttons defined in ecc.ui to handler methods
        self.btn_gen_key.clicked.connect(self.handle_generate_key)
        self.btn_sign.clicked.connect(self.handle_sign)
        self.btn_verify.clicked.connect(self.handle_verify)
        self.btn_back.clicked.connect(self.close)

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
