import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from uiloader import loadUi
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, NamedStyle
from pathlib import Path

class Ogrenci:
    def __init__(self, ogrno, sube, adi, ogretim, kitapcik, cevaplar) -> None:
        self.ogrno = ogrno
        self.adi = adi.strip()
        self.sube = sube
        self.ogretim = ogretim
        self.kitapcik = kitapcik
        self.cevaplar = cevaplar
        self.dogru = 0
        self.yanlis = 0
        self.bos = 0
        self.puan = 0

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainwindow.ui", self)
        self.dosyaAc.clicked.connect(self.dosya_ac)
        self.exceleAktar.clicked.connect(self.excele_aktar)
        self.students = []
        self.answers = {}
        self.question_count = {}
        self.set_table_headers()

    def excele_aktar(self):
        filename,_ = QFileDialog.getSaveFileName(self, "Excel'e Aktar", self.dersinAdi.text()+".xlsx", "Excel dosyaları(*.xlsx)")
        if not filename:
            return
        wb = Workbook()
        ws = wb.active
        for w,c in zip([90, 300, 50, 50, 50, 50, 50, 50],"ABCDEFGH"):
            ws.column_dimensions[c].width = w*0.13

        style = NamedStyle("Baslik")
        style.font = Font(bold=True)
        style.alignment = Alignment(horizontal="center")
        wb.add_named_style(style)

        ws.append(["Pamukkale Üniversitesi Mühendislik Fakültesi Test Sonuçları"])
        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=8)
        ws.cell(1,1).style = style
        ws.append([f"Dersin adı: {self.dersinAdi.text()}"])
        ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=8)
        ws.cell(2,1).style = style
        ws.append([])
        ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=8)
        ws.append(["Öğr.No.", "Adı", "Şube", "Kitapçık Türü", "Doğru", "Yanlış", "Boş", "Puan"])

        if self.ogrnoSirala.isChecked():
            ogrenciler = sorted(self.students, key=lambda ogr: ogr.ogrno)
        elif self.notSirala.isChecked():
            ogrenciler = sorted(self.students, key=lambda ogr: ogr.puan, reverse=True)
        else:
            ogrenciler = self.students

        for ogrenci in ogrenciler:
            ws.append([ogrenci.ogrno,
                       ogrenci.adi,
                       ogrenci.sube,
                       ogrenci.kitapcik,
                       ogrenci.dogru,
                       ogrenci.yanlis,
                       ogrenci.bos,
                       ogrenci.puan])
        wb.save(filename)


    def set_table_headers(self):
        self.notlarTablo.setColumnCount(8)
        self.notlarTablo.horizontalHeader().setStretchLastSection(True)
        self.notlarTablo.setHorizontalHeaderLabels(["Öğr.No.", "Adı", "Şube", "Kitapçık Türü", "Doğru", "Yanlış", "Boş", "Puan"])
        for i, w in enumerate([90, 300, 50, 50, 50, 50, 50, 50]):
            self.notlarTablo.setColumnWidth(i, w)

    def dosya_ac(self):
        filename,_ = QFileDialog.getOpenFileName(self, "Dosya Aç", ".", "Metin dosyaları(*.txt)")
        if not filename:
            return
        self.students = []
        self.answers = {}
        self.question_count = {}
        self.toplam_puan = self.toplamPuan.value()
        self.dersinAdi.setText(Path(filename).stem)
        with open(filename, encoding="ISO-8859-9") as f:
            lines = f.readlines()
        for line in lines:
            ogr, liste = self.process_line(line)
            if ogr:
                self.students.append(Ogrenci(*liste))
            else:
                self.answers[liste[0]] = liste[1]
                self.question_count[liste[0]] = len(list(filter(lambda a:a!=" ", liste[1])))
            # print(liste)
        self.kitapcikSayisi.setText(str(len(self.answers)))
        self.ogrenciSayisi.setText(str(len(self.students)))
        self.not_hesapla()
        self.not_goster()

    def not_goster(self):
        # self.notlarTablo.clear()
        self.notlarTablo.setRowCount(len(self.students))
        nt = self.notlarTablo
        if self.ogrnoSirala.isChecked():
            ogrenciler = sorted(self.students, key=lambda ogr: ogr.ogrno)
        elif self.notSirala.isChecked():
            ogrenciler = sorted(self.students, key=lambda ogr: ogr.puan, reverse=True)
        else:
            ogrenciler = self.students

        for i, ogrenci in enumerate(ogrenciler):
            nt.setItem(i, 0, QTableWidgetItem(ogrenci.ogrno))
            nt.setItem(i, 1, QTableWidgetItem(ogrenci.adi))
            nt.setItem(i, 2, QTableWidgetItem(ogrenci.sube))
            nt.setItem(i, 3, QTableWidgetItem(ogrenci.kitapcik))
            nt.setItem(i, 4, QTableWidgetItem(str(ogrenci.dogru)))
            nt.setItem(i, 5, QTableWidgetItem(str(ogrenci.yanlis)))
            nt.setItem(i, 6, QTableWidgetItem(str(ogrenci.bos)))
            nt.setItem(i, 7, QTableWidgetItem(str(ogrenci.puan)))

    def not_hesapla(self):
        for ogrenci in self.students:
            if ogrenci.kitapcik not in self.answers:
                kitapcik = next(iter(self.answers))
            else:
                kitapcik = ogrenci.kitapcik

            dogrular = self.answers[kitapcik]
            for o,a in zip(ogrenci.cevaplar, dogrular):
                if a != " ":
                    if o == a:
                        ogrenci.dogru += 1
                    elif o == " ":
                        ogrenci.bos += 1
                    else:
                        ogrenci.yanlis += 1
            ogrenci.puan = round(ogrenci.dogru/self.question_count[kitapcik]*self.toplam_puan)
            # print(ogrenci)


    def process_line(self, line):
        if line[11:16] == "CEVAP":
            return False, [line[36], line[37:137]]
        else:
            return True, [line[:8], line[8:11], line[11:35], line[35], line[36], line[37:137]]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
