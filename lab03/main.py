import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

# Ensure the lab03 folder is in path for modules import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.rsa_window import RSAWindow
from ui.ecc_window import ECCWindow

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()
        
        # Load the UI file dynamically
        ui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui', 'main.ui')
        uic.loadUi(ui_path, self)
        
        self.rsa_window = None
        self.ecc_window = None
        
        self.init_connections()
        
    def init_connections(self):
        self.btn_rsa.clicked.connect(self.open_rsa_window)
        self.btn_ecc.clicked.connect(self.open_ecc_window)
        
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
