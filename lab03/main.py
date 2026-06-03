import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Ensure the lab03 folder is in path for modules import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.rsa_window import RSAWindow
from ui.ecc_window import ECCWindow

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab 03 - RSA & ECC Security Application")
        self.resize(500, 350)
        
        self.rsa_window = None
        self.ecc_window = None
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 40, 30, 40)
        layout.setSpacing(25)
        
        # Header Info
        header_layout = QVBoxLayout()
        header_layout.setSpacing(5)
        
        title_label = QLabel("Lab 03 - RSA & ECC Security Application")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #5865f2; margin-bottom: 5px;")
        
        author_label = QLabel("Sinh viên: Lê Việt Đức - MSSV: 0533 - Lớp: 23DTHA4")
        author_label.setAlignment(Qt.AlignCenter)
        author_label.setStyleSheet("font-size: 13px; color: #b9bbbe;")
        
        course_label = QLabel("Môn: Thực hành Bảo mật thông tin nâng cao")
        course_label.setAlignment(Qt.AlignCenter)
        course_label.setStyleSheet("font-size: 13px; color: #b9bbbe; font-style: italic;")
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(author_label)
        header_layout.addWidget(course_label)
        layout.addLayout(header_layout)
        
        # Action Buttons
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(15)
        
        self.btn_rsa = QPushButton("1. RSA Encryption / Decryption")
        self.btn_rsa.setCursor(Qt.PointingHandCursor)
        self.btn_rsa.setStyleSheet("padding: 15px; font-size: 14px; text-align: left; padding-left: 25px;")
        self.btn_rsa.clicked.connect(self.open_rsa_window)
        btn_layout.addWidget(self.btn_rsa)
        
        self.btn_ecc = QPushButton("2. ECC Digital Signature")
        self.btn_ecc.setCursor(Qt.PointingHandCursor)
        self.btn_ecc.setStyleSheet("padding: 15px; font-size: 14px; text-align: left; padding-left: 25px;")
        self.btn_ecc.clicked.connect(self.open_ecc_window)
        btn_layout.addWidget(self.btn_ecc)
        
        layout.addLayout(btn_layout)
        
        # Footer
        footer_label = QLabel("Chọn một chức năng để bắt đầu")
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("color: #72767d; font-size: 11px;")
        layout.addWidget(footer_label)
        
    def open_rsa_window(self):
        if not self.rsa_window:
            self.rsa_window = RSAWindow()
        self.rsa_window.show()
        self.rsa_window.raise_()
        self.rsa_window.activateWindow()
        
    def open_ecc_window(self):
        if not self.ecc_window:
            self.ecc_window = ECCWindow()
        self.ecc_window.show()
        self.ecc_window.raise_()
        self.ecc_window.activateWindow()

def main():
    app = QApplication(sys.argv)
    
    # Premium Dark Theme Stylesheet
    dark_stylesheet = """
    QWidget {
        background-color: #1e1e24;
        color: #e4e4e6;
        font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    }
    
    QTextEdit, QLineEdit {
        background-color: #2b2b36;
        border: 1px solid #3f3f52;
        border-radius: 6px;
        padding: 8px;
        color: #ffffff;
        selection-background-color: #5865f2;
    }
    
    QTextEdit:focus, QLineEdit:focus {
        border: 1px solid #5865f2;
    }
    
    QPushButton {
        background-color: #5865f2;
        border: none;
        border-radius: 6px;
        color: white;
        font-weight: bold;
        padding: 10px 18px;
    }
    
    QPushButton:hover {
        background-color: #4752c4;
    }
    
    QPushButton:pressed {
        background-color: #3c45a5;
    }
    
    QLabel {
        font-weight: bold;
        color: #b9bbbe;
    }
    
    QMessageBox {
        background-color: #2f3136;
        color: #ffffff;
    }
    
    QMessageBox QLabel {
        color: #ffffff;
        font-weight: normal;
    }
    
    QMessageBox QPushButton {
        background-color: #4f545c;
        min-width: 80px;
    }
    
    QMessageBox QPushButton:hover {
        background-color: #686d73;
    }
    """
    
    app.setStyleSheet(dark_stylesheet)
    
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
