# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QToolBox, QVBoxLayout,
    QWidget)

class Ui_Asterisk_Extractor(object):
    def setupUi(self, Asterisk_Extractor):
        if not Asterisk_Extractor.objectName():
            Asterisk_Extractor.setObjectName(u"Asterisk_Extractor")
        Asterisk_Extractor.resize(835, 610)
        Asterisk_Extractor.setMinimumSize(QSize(835, 560))
        self.actionOpen = QAction(Asterisk_Extractor)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(Asterisk_Extractor)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(Asterisk_Extractor)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSaveToFile = QAction(Asterisk_Extractor)
        self.actionSaveToFile.setObjectName(u"actionSaveToFile")
        self.centralwidget = QWidget(Asterisk_Extractor)
        self.centralwidget.setObjectName(u"centralwidget")
        self._2 = QVBoxLayout(self.centralwidget)
        self._2.setObjectName(u"_2")
        self.tabWidget_CDRold = QTabWidget(self.centralwidget)
        self.tabWidget_CDRold.setObjectName(u"tabWidget_CDRold")
        self.tabCal = QWidget()
        self.tabCal.setObjectName(u"tabCal")
        self._3 = QVBoxLayout(self.tabCal)
        self._3.setObjectName(u"_3")
        self.toolBox = QToolBox(self.tabCal)
        self.toolBox.setObjectName(u"toolBox")
        self.pageCalendar = QWidget()
        self.pageCalendar.setObjectName(u"pageCalendar")
        self.pageCalendar.setGeometry(QRect(0, 0, 803, 432))
        self.gridLayout = QGridLayout(self.pageCalendar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_db = QLabel(self.pageCalendar)
        self.label_db.setObjectName(u"label_db")

        self.gridLayout.addWidget(self.label_db, 0, 0, 1, 1)

        self.label_db_2 = QLabel(self.pageCalendar)
        self.label_db_2.setObjectName(u"label_db_2")

        self.gridLayout.addWidget(self.label_db_2, 0, 1, 1, 1)

        self.calendar_db = QCalendarWidget(self.pageCalendar)
        self.calendar_db.setObjectName(u"calendar_db")
        self.calendar_db.setGridVisible(True)

        self.gridLayout.addWidget(self.calendar_db, 1, 0, 1, 1)

        self.calendar_de = QCalendarWidget(self.pageCalendar)
        self.calendar_de.setObjectName(u"calendar_de")
        self.calendar_de.setGridVisible(True)

        self.gridLayout.addWidget(self.calendar_de, 1, 1, 1, 1)

        self.toolBox.addItem(self.pageCalendar, u"Calendar")
        self.CDR_opt = QWidget()
        self.CDR_opt.setObjectName(u"CDR_opt")
        self.CDR_opt.setGeometry(QRect(0, 0, 803, 432))
        self._5 = QVBoxLayout(self.CDR_opt)
        self._5.setObjectName(u"_5")
        self.frame_3 = QFrame(self.CDR_opt)
        self.frame_3.setObjectName(u"frame_3")
        self._6 = QVBoxLayout(self.frame_3)
        self._6.setObjectName(u"_6")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self._6.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")

        self._6.addWidget(self.progressBar)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self._7 = QGridLayout(self.frame_4)
        self._7.setObjectName(u"_7")
        self.label_number = QLabel(self.frame_4)
        self.label_number.setObjectName(u"label_number")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_number.sizePolicy().hasHeightForWidth())
        self.label_number.setSizePolicy(sizePolicy)

        self._7.addWidget(self.label_number, 0, 0, 1, 1)

        self.textEditNumber = QTextEdit(self.frame_4)
        self.textEditNumber.setObjectName(u"textEditNumber")
        self.textEditNumber.setMaximumSize(QSize(100, 16777215))

        self._7.addWidget(self.textEditNumber, 1, 0, 3, 1)

        self.widget_triger = QWidget(self.frame_4)
        self.widget_triger.setObjectName(u"widget_triger")
        self._8 = QVBoxLayout(self.widget_triger)
        self._8.setObjectName(u"_8")
        self.comboBox_arr = QComboBox(self.widget_triger)
        self.comboBox_arr.addItem("")
        self.comboBox_arr.addItem("")
        self.comboBox_arr.setObjectName(u"comboBox_arr")

        self._8.addWidget(self.comboBox_arr)

        self.Button_execute = QPushButton(self.widget_triger)
        self.Button_execute.setObjectName(u"Button_execute")

        self._8.addWidget(self.Button_execute)

        self.Button_Clean = QPushButton(self.widget_triger)
        self.Button_Clean.setObjectName(u"Button_Clean")

        self._8.addWidget(self.Button_Clean)

        self.Button_test = QPushButton(self.widget_triger)
        self.Button_test.setObjectName(u"Button_test")

        self._8.addWidget(self.Button_test)


        self._7.addWidget(self.widget_triger, 1, 4, 1, 1)

        self.label_alert = QLabel(self.frame_4)
        self.label_alert.setObjectName(u"label_alert")

        self._7.addWidget(self.label_alert, 0, 1, 1, 1)

        self.label_triger = QLabel(self.frame_4)
        self.label_triger.setObjectName(u"label_triger")

        self._7.addWidget(self.label_triger, 0, 4, 1, 1)

        self.tableWidgetResult = QTableWidget(self.frame_4)
        self.tableWidgetResult.setObjectName(u"tableWidgetResult")
        self.tableWidgetResult.setMinimumSize(QSize(0, 160))

        self._7.addWidget(self.tableWidgetResult, 1, 1, 1, 3)

        self.textBrowser = QTextBrowser(self.frame_4)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        self.textBrowser.setBaseSize(QSize(0, 0))

        self._7.addWidget(self.textBrowser, 3, 1, 1, 4)


        self._6.addWidget(self.frame_4)


        self._5.addWidget(self.frame_3)

        self.toolBox.addItem(self.CDR_opt, u"Option")

        self._3.addWidget(self.toolBox)

        self.tabWidget_CDRold.addTab(self.tabCal, "")
        self.tabTool = QWidget()
        self.tabTool.setObjectName(u"tabTool")
        self._9 = QVBoxLayout(self.tabTool)
        self._9.setObjectName(u"_9")
        self.frame_2 = QFrame(self.tabTool)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self._11 = QFormLayout(self.frame)
        self._11.setObjectName(u"_11")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self._11.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_2_SNember = QLineEdit(self.frame)
        self.lineEdit_2_SNember.setObjectName(u"lineEdit_2_SNember")

        self._11.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2_SNember)

        self.textEdit_2_PhoneInfo = QTextEdit(self.frame)
        self.textEdit_2_PhoneInfo.setObjectName(u"textEdit_2_PhoneInfo")

        self._11.setWidget(1, QFormLayout.FieldRole, self.textEdit_2_PhoneInfo)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self._10 = QVBoxLayout(self.widget)
        self._10.setObjectName(u"_10")
        self.Button_2_SearchIp = QPushButton(self.widget)
        self.Button_2_SearchIp.setObjectName(u"Button_2_SearchIp")

        self._10.addWidget(self.Button_2_SearchIp)

        self.label_2_openLink = QLabel(self.widget)
        self.label_2_openLink.setObjectName(u"label_2_openLink")
        self.label_2_openLink.setEnabled(False)

        self._10.addWidget(self.label_2_openLink)

        self.pushButton_2_ModelPhone = QPushButton(self.widget)
        self.pushButton_2_ModelPhone.setObjectName(u"pushButton_2_ModelPhone")
        self.pushButton_2_ModelPhone.setEnabled(True)

        self._10.addWidget(self.pushButton_2_ModelPhone)

        self.pushButton_2_BanIp = QPushButton(self.widget)
        self.pushButton_2_BanIp.setObjectName(u"pushButton_2_BanIp")

        self._10.addWidget(self.pushButton_2_BanIp)

        self.pushButton_2_test = QPushButton(self.widget)
        self.pushButton_2_test.setObjectName(u"pushButton_2_test")

        self._10.addWidget(self.pushButton_2_test)


        self._11.setWidget(1, QFormLayout.LabelRole, self.widget)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 2, 1)

        self.textBrowser_Tool_Alert = QTextBrowser(self.frame_2)
        self.textBrowser_Tool_Alert.setObjectName(u"textBrowser_Tool_Alert")

        self.gridLayout_5.addWidget(self.textBrowser_Tool_Alert, 4, 0, 1, 1)


        self._9.addWidget(self.frame_2)

        self.tabWidget_CDRold.addTab(self.tabTool, "")
        self.tabChannel = QWidget()
        self.tabChannel.setObjectName(u"tabChannel")
        self.verticalLayout = QVBoxLayout(self.tabChannel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.tabChannel)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser_3_ChannelBrowser = QTextBrowser(self.widget_2)
        self.textBrowser_3_ChannelBrowser.setObjectName(u"textBrowser_3_ChannelBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser_3_ChannelBrowser)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Button_3_ChanAct = QPushButton(self.frame_5)
        self.Button_3_ChanAct.setObjectName(u"Button_3_ChanAct")

        self.horizontalLayout.addWidget(self.Button_3_ChanAct)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Button_CS_down = QPushButton(self.frame_6)
        self.Button_CS_down.setObjectName(u"Button_CS_down")

        self.horizontalLayout_2.addWidget(self.Button_CS_down)

        self.lineEdit_3_CS_down = QLineEdit(self.frame_6)
        self.lineEdit_3_CS_down.setObjectName(u"lineEdit_3_CS_down")

        self.horizontalLayout_2.addWidget(self.lineEdit_3_CS_down)

        self.label_3_CS_down = QLabel(self.frame_6)
        self.label_3_CS_down.setObjectName(u"label_3_CS_down")

        self.horizontalLayout_2.addWidget(self.label_3_CS_down)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.widget_2)

        self.tabWidget_CDRold.addTab(self.tabChannel, "")

        self._2.addWidget(self.tabWidget_CDRold)

        Asterisk_Extractor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Asterisk_Extractor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 835, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Asterisk_Extractor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Asterisk_Extractor)
        self.statusbar.setObjectName(u"statusbar")
        Asterisk_Extractor.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSaveToFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(Asterisk_Extractor)
        self.actionExit.triggered.connect(Asterisk_Extractor.close)

        self.tabWidget_CDRold.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Asterisk_Extractor)
    # setupUi

    def retranslateUi(self, Asterisk_Extractor):
        Asterisk_Extractor.setWindowTitle(QCoreApplication.translate("Asterisk_Extractor", u"Asterisk Extractor", None))
        self.actionOpen.setText(QCoreApplication.translate("Asterisk_Extractor", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("Asterisk_Extractor", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("Asterisk_Extractor", u"About", None))
        self.actionSaveToFile.setText(QCoreApplication.translate("Asterisk_Extractor", u"SaveToFile", None))
        self.label_db.setText(QCoreApplication.translate("Asterisk_Extractor", u"Begin Data", None))
        self.label_db_2.setText(QCoreApplication.translate("Asterisk_Extractor", u"label_de", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageCalendar), QCoreApplication.translate("Asterisk_Extractor", u"Calendar", None))
        self.label_3.setText(QCoreApplication.translate("Asterisk_Extractor", u"...", None))
        self.label_number.setText(QCoreApplication.translate("Asterisk_Extractor", u"Number", None))
        self.comboBox_arr.setItemText(0, QCoreApplication.translate("Asterisk_Extractor", u"\u0432\u0445\u043e\u0434\u044f\u0449\u0438\u0435", None))
        self.comboBox_arr.setItemText(1, QCoreApplication.translate("Asterisk_Extractor", u"\u0438\u0441\u0445\u043e\u0434\u044f\u0449\u0438\u0435", None))

        self.Button_execute.setText(QCoreApplication.translate("Asterisk_Extractor", u"Execute", None))
        self.Button_Clean.setText(QCoreApplication.translate("Asterisk_Extractor", u"Clean", None))
        self.Button_test.setText(QCoreApplication.translate("Asterisk_Extractor", u"TestFuncButton", None))
        self.label_alert.setText(QCoreApplication.translate("Asterisk_Extractor", u"Alert Output", None))
        self.label_triger.setText(QCoreApplication.translate("Asterisk_Extractor", u"Triger", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.CDR_opt), QCoreApplication.translate("Asterisk_Extractor", u"Option", None))
        self.tabWidget_CDRold.setTabText(self.tabWidget_CDRold.indexOf(self.tabCal), QCoreApplication.translate("Asterisk_Extractor", u"CDR", None))
        self.label.setText(QCoreApplication.translate("Asterisk_Extractor", u"Phone Number:", None))
        self.Button_2_SearchIp.setText(QCoreApplication.translate("Asterisk_Extractor", u"SearchIp", None))
        self.label_2_openLink.setText(QCoreApplication.translate("Asterisk_Extractor", u"Link", None))
        self.pushButton_2_ModelPhone.setText(QCoreApplication.translate("Asterisk_Extractor", u"ModelPhone", None))
        self.pushButton_2_BanIp.setText(QCoreApplication.translate("Asterisk_Extractor", u"bannet ip", None))
        self.pushButton_2_test.setText(QCoreApplication.translate("Asterisk_Extractor", u"...", None))
        self.tabWidget_CDRold.setTabText(self.tabWidget_CDRold.indexOf(self.tabTool), QCoreApplication.translate("Asterisk_Extractor", u"PhoneInfo", None))
        self.Button_3_ChanAct.setText(QCoreApplication.translate("Asterisk_Extractor", u"Scan Channels", None))
        self.Button_CS_down.setText(QCoreApplication.translate("Asterisk_Extractor", u"Down Channel", None))
        self.label_3_CS_down.setText("")
        self.tabWidget_CDRold.setTabText(self.tabWidget_CDRold.indexOf(self.tabChannel), QCoreApplication.translate("Asterisk_Extractor", u"Channel", None))
        self.menuFile.setTitle(QCoreApplication.translate("Asterisk_Extractor", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Asterisk_Extractor", u"Help", None))
    # retranslateUi

