from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

import os, sys, glob

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")  
        self.resize(800, 600)

        icon_file = self.find_icon_file()
        if icon_file: self.setWindowIcon(QIcon(icon_file))

    def find_icon_file(self) -> str:
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icons = glob.glob(os.path.join(base_path, "*.ico"))
        if icons: return icons[0] 
        return None
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
