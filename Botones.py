from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Botones Personalizados")
        self.setGeometry(100, 100, 300, 200)
        
        
        layout = QVBoxLayout()
        
        
        button1 = QPushButton("Button 1")
        button1.setStyleSheet(self.button_style())
        layout.addWidget(button1)
        
        button2 = QPushButton("Button 2")
        button2.setStyleSheet(self.button_style())
        layout.addWidget(button2)
        
        button3 = QPushButton("Button 3")
        button3.setStyleSheet(self.button_style())
        layout.addWidget(button3)
        
        self.setLayout(layout)

    def button_style(self):
        return """
        QPushButton {
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 20px;
            background: qlineargradient(
                spread: pad,
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ff6ec4, stop: 1 #7873f5
            );
        }
        QPushButton:hover {
            background: qlineargradient(
                spread: pad,
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ff72b6, stop: 1 #6c6ed5
            );
        }
        QPushButton:pressed {
            background: qlineargradient(
                spread: pad,
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 #ff5ea6, stop: 1 #5859c4
            );
        }
        """


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
