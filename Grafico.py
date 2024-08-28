import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Mi Primera Ventana')
window.setGeometry(100, 100, 600, 400)

layout = QVBoxLayout()

button = QPushButton('Presióname')
layout.addWidget(button)

window.setLayout(layout) 

window.show()

sys.exit(app.exec())