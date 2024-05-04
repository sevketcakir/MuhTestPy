# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.soruSayisi = QSpinBox(self.centralwidget)
        self.soruSayisi.setObjectName(u"soruSayisi")
        self.soruSayisi.setEnabled(False)
        self.soruSayisi.setReadOnly(False)
        self.soruSayisi.setValue(40)

        self.horizontalLayout_3.addWidget(self.soruSayisi)

        self.otomatikAlgila = QCheckBox(self.centralwidget)
        self.otomatikAlgila.setObjectName(u"otomatikAlgila")
        self.otomatikAlgila.setEnabled(False)
        self.otomatikAlgila.setChecked(True)

        self.horizontalLayout_3.addWidget(self.otomatikAlgila)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.toplamPuan = QSpinBox(self.centralwidget)
        self.toplamPuan.setObjectName(u"toplamPuan")
        self.toplamPuan.setMaximum(200)
        self.toplamPuan.setValue(100)

        self.horizontalLayout_4.addWidget(self.toplamPuan)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.kitapcikSayisi = QLabel(self.centralwidget)
        self.kitapcikSayisi.setObjectName(u"kitapcikSayisi")
        palette = QPalette()
        brush = QBrush(QColor(85, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        brush2 = QBrush(QColor(190, 190, 190, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.kitapcikSayisi.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.kitapcikSayisi.setFont(font)

        self.horizontalLayout_5.addWidget(self.kitapcikSayisi)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.ogrenciSayisi = QLabel(self.centralwidget)
        self.ogrenciSayisi.setObjectName(u"ogrenciSayisi")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.ogrenciSayisi.setPalette(palette1)
        self.ogrenciSayisi.setFont(font)

        self.horizontalLayout_5.addWidget(self.ogrenciSayisi)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.dosyaAc = QPushButton(self.centralwidget)
        self.dosyaAc.setObjectName(u"dosyaAc")
        self.dosyaAc.setMinimumSize(QSize(250, 60))

        self.horizontalLayout_2.addWidget(self.dosyaAc)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.dersinAdi = QLineEdit(self.centralwidget)
        self.dersinAdi.setObjectName(u"dersinAdi")

        self.horizontalLayout.addWidget(self.dersinAdi)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.notlarTablo = QTableWidget(self.centralwidget)
        self.notlarTablo.setObjectName(u"notlarTablo")
        self.notlarTablo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.notlarTablo.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.notlarTablo)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ogrnoSirala = QRadioButton(self.centralwidget)
        self.ogrnoSirala.setObjectName(u"ogrnoSirala")
        self.ogrnoSirala.setChecked(True)

        self.verticalLayout_3.addWidget(self.ogrnoSirala)

        self.notSirala = QRadioButton(self.centralwidget)
        self.notSirala.setObjectName(u"notSirala")

        self.verticalLayout_3.addWidget(self.notSirala)

        self.pusulayaUygun = QCheckBox(self.centralwidget)
        self.pusulayaUygun.setObjectName(u"pusulayaUygun")

        self.verticalLayout_3.addWidget(self.pusulayaUygun)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.exceleAktar = QPushButton(self.centralwidget)
        self.exceleAktar.setObjectName(u"exceleAktar")
        self.exceleAktar.setMinimumSize(QSize(0, 60))

        self.horizontalLayout_6.addWidget(self.exceleAktar)


        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.dersinAdi, self.notlarTablo)
        QWidget.setTabOrder(self.notlarTablo, self.dosyaAc)
        QWidget.setTabOrder(self.dosyaAc, self.otomatikAlgila)
        QWidget.setTabOrder(self.otomatikAlgila, self.toplamPuan)
        QWidget.setTabOrder(self.toplamPuan, self.exceleAktar)
        QWidget.setTabOrder(self.exceleAktar, self.ogrnoSirala)
        QWidget.setTabOrder(self.ogrnoSirala, self.notSirala)
        QWidget.setTabOrder(self.notSirala, self.pusulayaUygun)
        QWidget.setTabOrder(self.pusulayaUygun, self.soruSayisi)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PA\u00dc M\u00fchendislik Fak\u00fcltesi Optik Okuyucu Program\u0131", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Soru Say\u0131s\u0131", None))
        self.otomatikAlgila.setText(QCoreApplication.translate("MainWindow", u"Otomatik alg\u0131la", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Toplam puan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Kitap\u00e7\u0131k say\u0131s\u0131", None))
        self.kitapcikSayisi.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011frenci Say\u0131s\u0131", None))
        self.ogrenciSayisi.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dosyaAc.setText(QCoreApplication.translate("MainWindow", u"Dosya A\u00e7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dersin Ad\u0131    ", None))
        self.ogrnoSirala.setText(QCoreApplication.translate("MainWindow", u"\u00d6\u011frenci No'ya g\u00f6re s\u0131rala", None))
        self.notSirala.setText(QCoreApplication.translate("MainWindow", u"Nota g\u00f6re s\u0131rala(azalan)", None))
        self.pusulayaUygun.setText(QCoreApplication.translate("MainWindow", u"Pusulaya uygun(\u00d6\u011fr.No., Not)", None))
        self.exceleAktar.setText(QCoreApplication.translate("MainWindow", u"Excel'e aktar", None))
    # retranslateUi

