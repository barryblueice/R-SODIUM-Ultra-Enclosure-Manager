# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ultra_enclosure_manager.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QWidget)
import usm_rc

class Ui_main_interface(object):
    def setupUi(self, main_interface):
        if not main_interface.objectName():
            main_interface.setObjectName(u"main_interface")
        main_interface.resize(494, 375)
        icon = QIcon()
        icon.addFile(u":/img/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        main_interface.setWindowIcon(icon)
        main_interface.setAutoFillBackground(True)
        main_interface.setStyleSheet(u"")
        self.label_2 = QLabel(main_interface)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 151, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(141, 70))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/img/logo.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overview_button = QPushButton(main_interface)
        self.overview_button.setObjectName(u"overview_button")
        self.overview_button.setGeometry(QRect(20, 130, 131, 51))
        font1 = QFont()
        font1.setPointSize(10)
        self.overview_button.setFont(font1)
        self.SATA_Interface_button = QPushButton(main_interface)
        self.SATA_Interface_button.setObjectName(u"SATA_Interface_button")
        self.SATA_Interface_button.setGeometry(QRect(20, 250, 131, 51))
        self.SATA_Interface_button.setFont(font1)
        self.boxmode_button = QPushButton(main_interface)
        self.boxmode_button.setObjectName(u"boxmode_button")
        self.boxmode_button.setGeometry(QRect(20, 190, 131, 51))
        self.boxmode_button.setFont(font1)
        self.boxmode_button.setAutoFillBackground(False)
        self.about_button = QPushButton(main_interface)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setGeometry(QRect(20, 310, 131, 51))
        self.about_button.setFont(font1)
        self.sataconfig = QGroupBox(main_interface)
        self.sataconfig.setObjectName(u"sataconfig")
        self.sataconfig.setEnabled(True)
        self.sataconfig.setGeometry(QRect(170, 10, 311, 351))
        font2 = QFont()
        font2.setItalic(False)
        self.sataconfig.setFont(font2)
        self.sataconfig.setAutoFillBackground(True)
        self.sataconfig.setCheckable(False)
        self.scrollArea_2 = QScrollArea(self.sataconfig)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, 0, 311, 351))
        self.scrollArea_2.setAutoFillBackground(True)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -121, 297, 470))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 470))
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 360, 53, 21))
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 355, 141, 31))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setItalic(False)
        self.label_3.setFont(font3)
        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 191, 41))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setItalic(False)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.powertime = QSpinBox(self.scrollAreaWidgetContents_2)
        self.powertime.setObjectName(u"powertime")
        self.powertime.setGeometry(QRect(150, 356, 61, 31))
        self.powertime.setMinimum(1)
        self.powertime.setMaximum(10)
        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 200, 271, 71))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.label_20.setFont(font5)
        self.label_20.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 74, 251, 131))
        self.widget.setAutoFillBackground(False)
        self.PM = QCheckBox(self.widget)
        self.PM.setObjectName(u"PM")
        self.PM.setGeometry(QRect(70, 100, 111, 19))
        self.PM.setAcceptDrops(False)
        self.PM.setChecked(True)
        self.PM.setAutoExclusive(True)
        self.JBOD = QCheckBox(self.widget)
        self.JBOD.setObjectName(u"JBOD")
        self.JBOD.setGeometry(QRect(70, 70, 111, 19))
        self.JBOD.setAutoExclusive(True)
        self.R0 = QCheckBox(self.widget)
        self.R0.setObjectName(u"R0")
        self.R0.setGeometry(QRect(70, 10, 80, 19))
        self.R0.setAutoExclusive(True)
        self.R1 = QCheckBox(self.widget)
        self.R1.setObjectName(u"R1")
        self.R1.setGeometry(QRect(70, 40, 80, 19))
        self.R1.setAutoExclusive(True)
        self.sata_execute = QPushButton(self.scrollAreaWidgetContents_2)
        self.sata_execute.setObjectName(u"sata_execute")
        self.sata_execute.setGeometry(QRect(200, 410, 91, 41))
        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 290, 270, 2))
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(70, 315, 171, 31))
        self.label_22.setFont(font4)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.boxmode = QGroupBox(main_interface)
        self.boxmode.setObjectName(u"boxmode")
        self.boxmode.setGeometry(QRect(170, 10, 311, 351))
        self.boxmode.setAutoFillBackground(True)
        self.scrollArea = QScrollArea(self.boxmode)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, 0, 311, 351))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -286, 297, 635))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(100, 635))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.boxmode_execute = QPushButton(self.scrollAreaWidgetContents)
        self.boxmode_execute.setObjectName(u"boxmode_execute")
        self.boxmode_execute.setGeometry(QRect(200, 580, 91, 41))
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 480, 171, 31))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 20, 171, 31))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.storageconfig = QCheckBox(self.scrollAreaWidgetContents)
        self.storageconfig.setObjectName(u"storageconfig")
        self.storageconfig.setGeometry(QRect(20, 520, 261, 21))
        self.storageconfig.setFont(font1)
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 220, 171, 31))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 260, 131, 161))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nvme_self_power_checkbox = QCheckBox(self.groupBox)
        self.nvme_self_power_checkbox.setObjectName(u"nvme_self_power_checkbox")
        self.nvme_self_power_checkbox.setGeometry(QRect(30, 40, 83, 19))
        self.nvme_self_power_checkbox.setChecked(True)
        self.nvme_self_power_checkbox.setAutoExclusive(False)
        self.sata1_self_power_checkbox = QCheckBox(self.groupBox)
        self.sata1_self_power_checkbox.setObjectName(u"sata1_self_power_checkbox")
        self.sata1_self_power_checkbox.setGeometry(QRect(30, 70, 83, 19))
        self.sata1_self_power_checkbox.setChecked(True)
        self.sata1_self_power_checkbox.setAutoExclusive(False)
        self.sata2_self_power_checkbox = QCheckBox(self.groupBox)
        self.sata2_self_power_checkbox.setObjectName(u"sata2_self_power_checkbox")
        self.sata2_self_power_checkbox.setGeometry(QRect(30, 100, 83, 19))
        self.sata2_self_power_checkbox.setChecked(True)
        self.sata2_self_power_checkbox.setAutoExclusive(False)
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(159, 260, 131, 161))
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata1_ext_power_checkbox = QCheckBox(self.groupBox_2)
        self.sata1_ext_power_checkbox.setObjectName(u"sata1_ext_power_checkbox")
        self.sata1_ext_power_checkbox.setGeometry(QRect(30, 70, 83, 19))
        self.sata1_ext_power_checkbox.setChecked(True)
        self.sata1_ext_power_checkbox.setAutoExclusive(False)
        self.sata2_ext_power_checkbox = QCheckBox(self.groupBox_2)
        self.sata2_ext_power_checkbox.setObjectName(u"sata2_ext_power_checkbox")
        self.sata2_ext_power_checkbox.setGeometry(QRect(30, 100, 83, 19))
        self.sata2_ext_power_checkbox.setChecked(True)
        self.sata2_ext_power_checkbox.setAutoExclusive(False)
        self.nvme_ext_power_checkbox = QCheckBox(self.groupBox_2)
        self.nvme_ext_power_checkbox.setObjectName(u"nvme_ext_power_checkbox")
        self.nvme_ext_power_checkbox.setGeometry(QRect(30, 40, 83, 19))
        self.nvme_ext_power_checkbox.setChecked(True)
        self.nvme_ext_power_checkbox.setAutoExclusive(False)
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 200, 270, 2))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 450, 270, 2))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet(u"background-color: rgb(170, 170, 170);")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 60, 271, 131))
        self.nvmeonly = QCheckBox(self.widget_2)
        self.nvmeonly.setObjectName(u"nvmeonly")
        self.nvmeonly.setGeometry(QRect(20, 40, 231, 21))
        self.nvmeonly.setFont(font1)
        self.nvmeonly.setAutoExclusive(True)
        self.combinemode = QCheckBox(self.widget_2)
        self.combinemode.setObjectName(u"combinemode")
        self.combinemode.setGeometry(QRect(20, 10, 231, 21))
        self.combinemode.setFont(font1)
        self.combinemode.setChecked(True)
        self.combinemode.setAutoExclusive(True)
        self.hubonly = QCheckBox(self.widget_2)
        self.hubonly.setObjectName(u"hubonly")
        self.hubonly.setGeometry(QRect(20, 100, 231, 21))
        self.hubonly.setFont(font1)
        self.hubonly.setAutoExclusive(True)
        self.sataonly = QCheckBox(self.widget_2)
        self.sataonly.setObjectName(u"sataonly")
        self.sataonly.setGeometry(QRect(20, 70, 231, 21))
        self.sataonly.setFont(font1)
        self.sataonly.setAutoExclusive(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.overview = QGroupBox(main_interface)
        self.overview.setObjectName(u"overview")
        self.overview.setGeometry(QRect(170, 10, 311, 351))
        self.overview.setAutoFillBackground(True)
        self.label_7 = QLabel(self.overview)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 40, 161, 31))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.overview)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 90, 151, 21))
        self.label_8.setFont(font1)
        self.nvme_status = QLabel(self.overview)
        self.nvme_status.setObjectName(u"nvme_status")
        self.nvme_status.setGeometry(QRect(200, 90, 71, 21))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.nvme_status.setFont(font6)
        self.nvme_status.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.nvme_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sata1_status = QLabel(self.overview)
        self.sata1_status.setObjectName(u"sata1_status")
        self.sata1_status.setGeometry(QRect(200, 120, 71, 21))
        self.sata1_status.setFont(font6)
        self.sata1_status.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sata1_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.overview)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 120, 151, 21))
        self.label_9.setFont(font1)
        self.sata2_status = QLabel(self.overview)
        self.sata2_status.setObjectName(u"sata2_status")
        self.sata2_status.setGeometry(QRect(200, 150, 71, 21))
        self.sata2_status.setFont(font6)
        self.sata2_status.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.sata2_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.overview)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 150, 151, 21))
        self.label_10.setFont(font1)
        self.ext_power_status = QLabel(self.overview)
        self.ext_power_status.setObjectName(u"ext_power_status")
        self.ext_power_status.setGeometry(QRect(200, 180, 71, 21))
        self.ext_power_status.setFont(font6)
        self.ext_power_status.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.ext_power_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.overview)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 180, 141, 21))
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ext_pwr_tips = QLabel(self.overview)
        self.ext_pwr_tips.setObjectName(u"ext_pwr_tips")
        self.ext_pwr_tips.setGeometry(QRect(30, 240, 261, 41))
        self.ext_pwr_tips.setFont(font6)
        self.ext_pwr_tips.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.ext_pwr_tips.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.about = QGroupBox(main_interface)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(170, 10, 311, 351))
        self.about.setAutoFillBackground(True)
        self.about.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.about)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(130, 50, 161, 91))
        self.label_15.setPixmap(QPixmap(u":/img/logo.svg"))
        self.label_15.setScaledContents(True)
        self.label_16 = QLabel(self.about)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 40, 100, 100))
        self.label_16.setPixmap(QPixmap(u":/img/icon-non-background.png"))
        self.label_16.setScaledContents(True)
        self.label_17 = QLabel(self.about)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(80, 170, 151, 16))
        self.label_17.setOpenExternalLinks(False)
        self.label_17.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.label_18 = QLabel(self.about)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 190, 291, 41))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextEditable|Qt.TextInteractionFlag.TextEditorInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_19 = QLabel(self.about)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 250, 291, 20))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.overview_button.raise_()
        self.label_2.raise_()
        self.SATA_Interface_button.raise_()
        self.boxmode_button.raise_()
        self.about_button.raise_()
        self.overview.raise_()
        self.sataconfig.raise_()
        self.boxmode.raise_()
        self.about.raise_()

        self.retranslateUi(main_interface)

        QMetaObject.connectSlotsByName(main_interface)
    # setupUi

    def retranslateUi(self, main_interface):
        main_interface.setWindowTitle(QCoreApplication.translate("main_interface", u"R-SODIUM Ultra SSD Enclosure Manager", None))
        self.label_2.setText("")
        self.overview_button.setText(QCoreApplication.translate("main_interface", u"Overview", None))
        self.SATA_Interface_button.setText(QCoreApplication.translate("main_interface", u"SATA Config", None))
        self.boxmode_button.setText(QCoreApplication.translate("main_interface", u"Enclosure Config", None))
        self.about_button.setText(QCoreApplication.translate("main_interface", u"About", None))
        self.sataconfig.setStyleSheet("")
        self.sataconfig.setTitle("")
        self.label_4.setText(QCoreApplication.translate("main_interface", u"second/s.", None))
        self.label_3.setText(QCoreApplication.translate("main_interface", u"SATA power-up after", None))
        self.label.setText(QCoreApplication.translate("main_interface", u"ASM1352R RAID Config", None))
        self.label_20.setText(QCoreApplication.translate("main_interface", u"Warning: ASM1352R with\n"
"unsupported firmware\n"
"may not support this function!", None))
        self.PM.setText(QCoreApplication.translate("main_interface", u" Normal", None))
        self.JBOD.setText(QCoreApplication.translate("main_interface", u" SPAN / JBOD", None))
        self.R0.setText(QCoreApplication.translate("main_interface", u" RAID 0", None))
        self.R1.setText(QCoreApplication.translate("main_interface", u" RAID 1", None))
        self.sata_execute.setText(QCoreApplication.translate("main_interface", u"Execute", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("main_interface", u"Other Configuration", None))
        self.boxmode.setStyleSheet("")
        self.boxmode.setTitle("")
        self.boxmode_execute.setText(QCoreApplication.translate("main_interface", u"Execute", None))
        self.label_6.setText(QCoreApplication.translate("main_interface", u"Other Configuration", None))
        self.label_5.setText(QCoreApplication.translate("main_interface", u"Enclosure Mode", None))
        self.storageconfig.setText(QCoreApplication.translate("main_interface", u"Keep mode config for next power up.", None))
        self.label_12.setText(QCoreApplication.translate("main_interface", u"Disk Onpower Config", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_interface", u"Self-Powered", None))
        self.nvme_self_power_checkbox.setText(QCoreApplication.translate("main_interface", u"NVMe", None))
        self.sata1_self_power_checkbox.setText(QCoreApplication.translate("main_interface", u"SATA1", None))
        self.sata2_self_power_checkbox.setText(QCoreApplication.translate("main_interface", u"SATA2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("main_interface", u"Ext-Powered", None))
        self.sata1_ext_power_checkbox.setText(QCoreApplication.translate("main_interface", u"SATA1", None))
        self.sata2_ext_power_checkbox.setText(QCoreApplication.translate("main_interface", u"SATA2", None))
        self.nvme_ext_power_checkbox.setText(QCoreApplication.translate("main_interface", u"NVMe", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.nvmeonly.setText(QCoreApplication.translate("main_interface", u"ASM2362 Only", None))
        self.combinemode.setText(QCoreApplication.translate("main_interface", u"Combine Mode", None))
        self.hubonly.setText(QCoreApplication.translate("main_interface", u"Hub Only (No disk connected)", None))
        self.sataonly.setText(QCoreApplication.translate("main_interface", u"ASM1352R Only", None))
        self.overview.setStyleSheet("")
        self.overview.setTitle("")
        self.label_7.setText(QCoreApplication.translate("main_interface", u"Overview", None))
        self.label_8.setText(QCoreApplication.translate("main_interface", u"NVMe onpower status:", None))
        self.nvme_status.setText(QCoreApplication.translate("main_interface", u"None", None))
        self.sata1_status.setText(QCoreApplication.translate("main_interface", u"None", None))
        self.label_9.setText(QCoreApplication.translate("main_interface", u"SATA1 onpower status:", None))
        self.sata2_status.setText(QCoreApplication.translate("main_interface", u"None", None))
        self.label_10.setText(QCoreApplication.translate("main_interface", u"SATA2 onpower status:", None))
        self.ext_power_status.setText(QCoreApplication.translate("main_interface", u"None", None))
        self.label_11.setText(QCoreApplication.translate("main_interface", u"External power status:", None))
        self.ext_pwr_tips.setText(QCoreApplication.translate("main_interface", u"Recommended to use external power\n"
"for better stability and performance.", None))
        self.about.setStyleSheet("")
        self.about.setTitle("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("main_interface", u"Open-sourced On Github:", None))
        self.label_18.setText(QCoreApplication.translate("main_interface", u"https://github.com/barryblueice/\n"
"R-SODIUM-Ultra-Enclosure-Manager", None))
        self.label_19.setText(QCoreApplication.translate("main_interface", u"Hope you enjoy my work! :)", None))
    # retranslateUi

