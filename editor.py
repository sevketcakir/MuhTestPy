import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QFileDialog, QPushButton, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt

class ExamEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sınav Dosyası Düzenleyici")
        self.resize(800, 600)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Table widget
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        # Buttons
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.load_button = QPushButton("Dosya Aç")
        self.load_button.clicked.connect(self.load_file)
        self.button_layout.addWidget(self.load_button)

        self.save_button = QPushButton("Farklı Kaydet")
        self.save_button.clicked.connect(self.save_file)
        self.button_layout.addWidget(self.save_button)

        self.file_data = []  # To hold the original data

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Sınav Dosyasını Aç", "", "Metin dosyaları (*.txt)")
        if not file_name:
            return

        try:
            with open(file_name, encoding="ISO-8859-9") as file:
                lines = file.readlines()

            self.file_data = lines
            self.populate_table(lines)

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya açılırken bir hata oluştu: {e}")

    def populate_table(self, lines):
        self.table.clear()

        column_headers = (
            ["Öğr.No.", "Şube", "Adı", "Öğretim", "Grup"] +
            [f"S{i+1}" for i in range(100)]
        )
        self.table.setColumnCount(len(column_headers))
        self.table.setRowCount(len(lines))
        self.table.setHorizontalHeaderLabels(column_headers)

        self.table.setColumnWidth(2, 200)
        for i in range(5, 105):
            self.table.setColumnWidth(i, 20)

        for row_idx, line in enumerate(lines):
            if line[11:16] == "CEVAP":
                # Cevap satırı
                group = line[36]
                answers = line[37:137]
                self.table.setItem(row_idx, 2, QTableWidgetItem("CEVAP"))
                self.table.setItem(row_idx, 4, QTableWidgetItem(group))
                for col_idx, answer in enumerate(answers):
                    item = QTableWidgetItem(answer if answer.strip() else " ")
                    self.table.setItem(row_idx, 5 + col_idx, item)
            else:
                # Öğrenci satırı
                student_number = line[:8]
                division = line[8:11]
                name = line[11:35]
                branch = line[35]
                group = line[36]
                answers = line[37:137]

                self.table.setItem(row_idx, 0, QTableWidgetItem(student_number))
                self.table.setItem(row_idx, 1, QTableWidgetItem(division))
                self.table.setItem(row_idx, 2, QTableWidgetItem(name.strip()))
                self.table.setItem(row_idx, 3, QTableWidgetItem(branch))
                self.table.setItem(row_idx, 4, QTableWidgetItem(group))

                for col_idx, answer in enumerate(answers):
                    item = QTableWidgetItem(answer if answer.strip() else " ")
                    self.table.setItem(row_idx, 5 + col_idx, item)

        # Tüm hücrelerin boş QTableWidgetItem olmasını sağla
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                if not self.table.item(row, col):
                    self.table.setItem(row, col, QTableWidgetItem(""))

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "", "Metin dosyaları (*.txt)")
        if not file_name:
            return

        try:
            with open(file_name, "w", encoding="ISO-8859-9") as file:
                for row in range(self.table.rowCount()):
                    student_number = self.table.item(row, 0).text().ljust(8) if self.table.item(row, 0) else " " * 8
                    division = self.table.item(row, 1).text().ljust(3) if self.table.item(row, 1) else " " * 3
                    name = self.table.item(row, 2).text().ljust(24) if self.table.item(row, 2) else " " * 24
                    branch = self.table.item(row, 3).text().ljust(1) if self.table.item(row, 3) else " "
                    group = self.table.item(row, 4).text().ljust(1) if self.table.item(row, 4) else " "

                    answers = [" "] * 100
                    for col in range(100):
                        item = self.table.item(row, 5 + col)
                        answers[col] = item.text() if item and item.text() != "" else " "
                    answers = "".join(answers)

                    line = f"{student_number}{division}{name}{branch}{group}{answers}\n"
                    file.write(line)

            QMessageBox.information(self, "Başarılı", "Dosya başarıyla kaydedildi.")

        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya kaydedilirken bir hata oluştu: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ExamEditor()
    editor.show()
    sys.exit(app.exec())
