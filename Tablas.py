from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Tabla de Precios Personalizada")
        self.setGeometry(100, 100, 600, 400)
        
        
        table = QTableWidget(10, 8)  
        table.setHorizontalHeaderLabels(["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7" ])
        table.setVerticalHeaderLabels(["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"])
        

        
        table.setStyleSheet(self.table_style())
        
        
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        
        table.horizontalHeader().setStretchLastSection(True)
        table.verticalHeader().setVisible(False)


        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)

    def table_style(self):
        return """
        QTableWidget {
            background-color: white;
            gridline-color: #ccc;
            font-size: 14px;
            font-weight: bold;
        }
        QTableWidget::item {
            border: none;
            padding: 15px;
            text-align: center;
        }
        QHeaderView::section {
            background-color: #323748;
            color: white;
            padding: 10px;
            font-size: 14px;
            border: none;
        }
        QTableWidget::item:selected {
            background-color: #6e83f5;
            color: white;
        }
        QTableWidget::item {
            background-color: transparent;
            color: black;
        }
        QTableWidget::item:nth-child(odd) {
            background-color: #f0f4ff;
        }
        QTableWidget::item:nth-child(even) {
            background-color: #ffffff;
        }
        """
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
