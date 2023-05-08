# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sys_blackwolf_cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QToolBox, QVBoxLayout, QWidget)
import images__rc
import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1077, 623)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1836, 16777215))
        MainWindow.setStyleSheet(u"\n"
"<RCC>\n"
"    <qresource prefix=\"/\">\n"
"        <file>mainwindow.ui</file>\n"
"    </qresource>\n"
"    <qresource prefix=\"/qss\">\n"
"        <file>meu_theme.qss</file>\n"
"    </qresource>\n"
"</RCC>")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_menu = QFrame(self.centralwidget)
        self.container_menu.setObjectName(u"container_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.container_menu.sizePolicy().hasHeightForWidth())
        self.container_menu.setSizePolicy(sizePolicy2)
        self.container_menu.setMaximumSize(QSize(200, 16777215))
        self.container_menu.setStyleSheet(u"")
        self.container_menu.setFrameShape(QFrame.StyledPanel)
        self.container_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.container_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_headmenubar = QFrame(self.container_menu)
        self.frame_headmenubar.setObjectName(u"frame_headmenubar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_headmenubar.sizePolicy().hasHeightForWidth())
        self.frame_headmenubar.setSizePolicy(sizePolicy3)
        self.frame_headmenubar.setMinimumSize(QSize(0, 55))
        self.frame_headmenubar.setFrameShape(QFrame.Box)
        self.frame_headmenubar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_headmenubar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_headmenubar)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lbl_menubar = QLabel(self.frame_headmenubar)
        self.lbl_menubar.setObjectName(u"lbl_menubar")

        self.horizontalLayout_3.addWidget(self.lbl_menubar)


        self.verticalLayout_3.addWidget(self.frame_headmenubar)

        self.fr_tbx_menubar = QFrame(self.container_menu)
        self.fr_tbx_menubar.setObjectName(u"fr_tbx_menubar")
        self.fr_tbx_menubar.setStyleSheet(u"")
        self.fr_tbx_menubar.setFrameShape(QFrame.Box)
        self.fr_tbx_menubar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_tbx_menubar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 10, 10, 10)
        self.tbx_menubar = QToolBox(self.fr_tbx_menubar)
        self.tbx_menubar.setObjectName(u"tbx_menubar")
        self.tbx_menubar.setEnabled(True)
        self.tbx_menubar.setStyleSheet(u"\n"
"\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px")
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        self.page_menu.setGeometry(QRect(0, 0, 157, 463))
        self.verticalLayout_6 = QVBoxLayout(self.page_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_home = QPushButton(self.page_menu)
        self.btn_home.setObjectName(u"btn_home")

        self.verticalLayout_6.addWidget(self.btn_home)

        self.btn_cadastro = QPushButton(self.page_menu)
        self.btn_cadastro.setObjectName(u"btn_cadastro")

        self.verticalLayout_6.addWidget(self.btn_cadastro)

        self.btn_Contatos = QPushButton(self.page_menu)
        self.btn_Contatos.setObjectName(u"btn_Contatos")

        self.verticalLayout_6.addWidget(self.btn_Contatos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tbx_menubar.addItem(self.page_menu, u"Menu")
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.page_sobre.setGeometry(QRect(0, 0, 157, 463))
        self.txtbrw_sobre = QTextBrowser(self.page_sobre)
        self.txtbrw_sobre.setObjectName(u"txtbrw_sobre")
        self.txtbrw_sobre.setGeometry(QRect(-10, 10, 161, 435))
        self.txtbrw_sobre.setMinimumSize(QSize(0, 0))
        self.txtbrw_sobre.setMaximumSize(QSize(16777215, 450))
        self.txtbrw_sobre.setLayoutDirection(Qt.LeftToRight)
        self.txtbrw_sobre.setFrameShape(QFrame.Box)
        self.txtbrw_sobre.setLineWrapMode(QTextEdit.WidgetWidth)
        self.tbx_menubar.addItem(self.page_sobre, u"Sobre")

        self.verticalLayout_4.addWidget(self.tbx_menubar)


        self.verticalLayout_3.addWidget(self.fr_tbx_menubar)


        self.horizontalLayout.addWidget(self.container_menu)

        self.container_center = QFrame(self.centralwidget)
        self.container_center.setObjectName(u"container_center")
        self.container_center.setStyleSheet(u"")
        self.container_center.setFrameShape(QFrame.Box)
        self.container_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container_center)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_header = QFrame(self.container_center)
        self.container_header.setObjectName(u"container_header")
        sizePolicy1.setHeightForWidth(self.container_header.sizePolicy().hasHeightForWidth())
        self.container_header.setSizePolicy(sizePolicy1)
        self.container_header.setMinimumSize(QSize(0, 55))
        self.container_header.setMaximumSize(QSize(16777215, 50))
        self.container_header.setFrameShape(QFrame.StyledPanel)
        self.container_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_header_btn = QFrame(self.container_header)
        self.fr_header_btn.setObjectName(u"fr_header_btn")
        sizePolicy3.setHeightForWidth(self.fr_header_btn.sizePolicy().hasHeightForWidth())
        self.fr_header_btn.setSizePolicy(sizePolicy3)
        self.fr_header_btn.setMinimumSize(QSize(0, 53))
        self.fr_header_btn.setMaximumSize(QSize(16777215, 16777215))
        self.fr_header_btn.setStyleSheet(u"")
        self.fr_header_btn.setFrameShape(QFrame.NoFrame)
        self.fr_header_btn.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.fr_header_btn)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 100, -1)
        self.btn_toggle = QPushButton(self.fr_header_btn)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy4.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy4)
        self.btn_toggle.setMinimumSize(QSize(5, 5))
        icon = QIcon()
        icon.addFile(u"images/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_toggle)

        self.lbl_head = QLabel(self.fr_header_btn)
        self.lbl_head.setObjectName(u"lbl_head")
        sizePolicy1.setHeightForWidth(self.lbl_head.sizePolicy().hasHeightForWidth())
        self.lbl_head.setSizePolicy(sizePolicy1)
        self.lbl_head.setMinimumSize(QSize(0, 30))
        self.lbl_head.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_4.addWidget(self.lbl_head)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addWidget(self.fr_header_btn)


        self.verticalLayout.addWidget(self.container_header)

        self.frame_4 = QFrame(self.container_center)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setStyleSheet(u"")
        self.page_cadastro = QWidget()
        self.page_cadastro.setObjectName(u"page_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.page_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabw_cadastro = QTabWidget(self.page_cadastro)
        self.tabw_cadastro.setObjectName(u"tabw_cadastro")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabw_cadastro.sizePolicy().hasHeightForWidth())
        self.tabw_cadastro.setSizePolicy(sizePolicy5)
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.verticalLayout_13 = QVBoxLayout(self.tab_cadastro)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.txt_empresascadastro = QLabel(self.tab_cadastro)
        self.txt_empresascadastro.setObjectName(u"txt_empresascadastro")
        self.txt_empresascadastro.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_13.addWidget(self.txt_empresascadastro)

        self.fr_form_empresas = QFrame(self.tab_cadastro)
        self.fr_form_empresas.setObjectName(u"fr_form_empresas")
        sizePolicy5.setHeightForWidth(self.fr_form_empresas.sizePolicy().hasHeightForWidth())
        self.fr_form_empresas.setSizePolicy(sizePolicy5)
        self.fr_form_empresas.setFrameShape(QFrame.StyledPanel)
        self.fr_form_empresas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.fr_form_empresas)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.form_empresas = QFrame(self.fr_form_empresas)
        self.form_empresas.setObjectName(u"form_empresas")
        sizePolicy2.setHeightForWidth(self.form_empresas.sizePolicy().hasHeightForWidth())
        self.form_empresas.setSizePolicy(sizePolicy2)
        self.form_empresas.setMaximumSize(QSize(16777215, 200))
        self.form_empresas.setFrameShape(QFrame.StyledPanel)
        self.form_empresas.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.form_empresas)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_email = QLineEdit(self.form_empresas)
        self.txt_email.setObjectName(u"txt_email")

        self.gridLayout_2.addWidget(self.txt_email, 4, 1, 1, 2)

        self.txt_municipio = QLineEdit(self.form_empresas)
        self.txt_municipio.setObjectName(u"txt_municipio")

        self.gridLayout_2.addWidget(self.txt_municipio, 3, 0, 1, 1)

        self.txt_telefone = QLineEdit(self.form_empresas)
        self.txt_telefone.setObjectName(u"txt_telefone")

        self.gridLayout_2.addWidget(self.txt_telefone, 4, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.form_empresas)
        self.txt_complemento.setObjectName(u"txt_complemento")

        self.gridLayout_2.addWidget(self.txt_complemento, 2, 1, 1, 1)

        self.btn_cadastrar = QPushButton(self.form_empresas)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(221, 28))

        self.gridLayout_2.addWidget(self.btn_cadastrar, 5, 1, 1, 1, Qt.AlignHCenter)

        self.txt_cnpj = QLineEdit(self.form_empresas)
        self.txt_cnpj.setObjectName(u"txt_cnpj")

        self.gridLayout_2.addWidget(self.txt_cnpj, 0, 0, 1, 1)

        self.txt_bairro = QLineEdit(self.form_empresas)
        self.txt_bairro.setObjectName(u"txt_bairro")

        self.gridLayout_2.addWidget(self.txt_bairro, 2, 2, 1, 1)

        self.txt_cep = QLineEdit(self.form_empresas)
        self.txt_cep.setObjectName(u"txt_cep")

        self.gridLayout_2.addWidget(self.txt_cep, 3, 2, 1, 1)

        self.txt_nmempresarial = QLineEdit(self.form_empresas)
        self.txt_nmempresarial.setObjectName(u"txt_nmempresarial")

        self.gridLayout_2.addWidget(self.txt_nmempresarial, 0, 1, 1, 2)

        self.txt_uf = QLineEdit(self.form_empresas)
        self.txt_uf.setObjectName(u"txt_uf")

        self.gridLayout_2.addWidget(self.txt_uf, 3, 1, 1, 1)

        self.txt_numero = QLineEdit(self.form_empresas)
        self.txt_numero.setObjectName(u"txt_numero")

        self.gridLayout_2.addWidget(self.txt_numero, 2, 0, 1, 1)

        self.txt_logradouro = QLineEdit(self.form_empresas)
        self.txt_logradouro.setObjectName(u"txt_logradouro")

        self.gridLayout_2.addWidget(self.txt_logradouro, 1, 0, 1, 3)


        self.verticalLayout_15.addWidget(self.form_empresas)


        self.verticalLayout_13.addWidget(self.fr_form_empresas, 0, Qt.AlignTop)

        self.tabw_cadastro.addTab(self.tab_cadastro, "")
        self.tab_empresas = QWidget()
        self.tab_empresas.setObjectName(u"tab_empresas")
        self.verticalLayout_11 = QVBoxLayout(self.tab_empresas)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tbl_head = QLabel(self.tab_empresas)
        self.tbl_head.setObjectName(u"tbl_head")
        self.tbl_head.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.tbl_head)

        self.hlt_tblw_empresas = QHBoxLayout()
        self.hlt_tblw_empresas.setSpacing(0)
        self.hlt_tblw_empresas.setObjectName(u"hlt_tblw_empresas")
        self.fr_tblw_intern = QFrame(self.tab_empresas)
        self.fr_tblw_intern.setObjectName(u"fr_tblw_intern")
        self.fr_tblw_intern.setFrameShape(QFrame.NoFrame)
        self.fr_tblw_intern.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.fr_tblw_intern)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tbwl_empresas = QTableWidget(self.fr_tblw_intern)
        if (self.tbwl_empresas.columnCount() < 11):
            self.tbwl_empresas.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbwl_empresas.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tbwl_empresas.rowCount() < 10):
            self.tbwl_empresas.setRowCount(10)
        self.tbwl_empresas.setObjectName(u"tbwl_empresas")
        self.tbwl_empresas.setFrameShape(QFrame.NoFrame)
        self.tbwl_empresas.setFrameShadow(QFrame.Plain)
        self.tbwl_empresas.setRowCount(10)

        self.verticalLayout_12.addWidget(self.tbwl_empresas)


        self.hlt_tblw_empresas.addWidget(self.fr_tblw_intern)

        self.fr_tblw_rigthbar_2 = QFrame(self.tab_empresas)
        self.fr_tblw_rigthbar_2.setObjectName(u"fr_tblw_rigthbar_2")
        self.fr_tblw_rigthbar_2.setFrameShape(QFrame.NoFrame)
        self.fr_tblw_rigthbar_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.fr_tblw_rigthbar_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.btn_gerarexecel = QPushButton(self.fr_tblw_rigthbar_2)
        self.btn_gerarexecel.setObjectName(u"btn_gerarexecel")

        self.verticalLayout_10.addWidget(self.btn_gerarexecel)

        self.btn_alterar = QPushButton(self.fr_tblw_rigthbar_2)
        self.btn_alterar.setObjectName(u"btn_alterar")

        self.verticalLayout_10.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.fr_tblw_rigthbar_2)
        self.btn_excluir.setObjectName(u"btn_excluir")

        self.verticalLayout_10.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.hlt_tblw_empresas.addWidget(self.fr_tblw_rigthbar_2)


        self.verticalLayout_11.addLayout(self.hlt_tblw_empresas)

        self.tabw_cadastro.addTab(self.tab_empresas, "")

        self.verticalLayout_9.addWidget(self.tabw_cadastro)

        self.stackedWidget.addWidget(self.page_cadastro)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.pg_home)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_16 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.txt_contatos = QLabel(self.pg_contatos)
        self.txt_contatos.setObjectName(u"txt_contatos")
        self.txt_contatos.setMaximumSize(QSize(16777215, 50))
        self.txt_contatos.setFrameShape(QFrame.NoFrame)
        self.txt_contatos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.txt_contatos)

        self.fr_contatos = QFrame(self.pg_contatos)
        self.fr_contatos.setObjectName(u"fr_contatos")
        self.fr_contatos.setFrameShape(QFrame.StyledPanel)
        self.fr_contatos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.fr_contatos)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lbl_17 = QLabel(self.fr_contatos)
        self.lbl_17.setObjectName(u"lbl_17")
        self.lbl_17.setFrameShape(QFrame.Box)

        self.verticalLayout_14.addWidget(self.lbl_17)

        self.lbl_email = QLabel(self.fr_contatos)
        self.lbl_email.setObjectName(u"lbl_email")
        self.lbl_email.setFrameShape(QFrame.Box)

        self.verticalLayout_14.addWidget(self.lbl_email)

        self.lbl_in = QLabel(self.fr_contatos)
        self.lbl_in.setObjectName(u"lbl_in")
        self.lbl_in.setFrameShape(QFrame.Box)

        self.verticalLayout_14.addWidget(self.lbl_in)


        self.verticalLayout_16.addWidget(self.fr_contatos)

        self.stackedWidget.addWidget(self.pg_contatos)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_4)

        self.container_footer = QFrame(self.container_center)
        self.container_footer.setObjectName(u"container_footer")
        sizePolicy1.setHeightForWidth(self.container_footer.sizePolicy().hasHeightForWidth())
        self.container_footer.setSizePolicy(sizePolicy1)
        self.container_footer.setMaximumSize(QSize(16777215, 50))
        self.container_footer.setFrameShape(QFrame.StyledPanel)
        self.container_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container_footer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 10, 10)
        self.lbl_footer = QLabel(self.container_footer)
        self.lbl_footer.setObjectName(u"lbl_footer")
        self.lbl_footer.setFrameShape(QFrame.NoFrame)
        self.lbl_footer.setFrameShadow(QFrame.Plain)

        self.verticalLayout_2.addWidget(self.lbl_footer, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.container_footer)


        self.horizontalLayout.addWidget(self.container_center)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tbx_menubar.setCurrentIndex(1)
        self.tbx_menubar.layout().setSpacing(7)
        self.stackedWidget.setCurrentIndex(1)
        self.tabw_cadastro.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/images/icons/icon_bw_resized.png\"/></p></body></html>", None))
        self.lbl_menubar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\"> BlackWolf </span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.btn_Contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.tbx_menubar.setItemText(self.tbx_menubar.indexOf(self.page_menu), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.txtbrw_sobre.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Este sistema faz consulta do CNPJ utilizando API da receita federal e faz o cadastro em um banco de dados SQLITE3. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Objetivo desse sistema \u00e9 demosntrar conhecimento de como utiliza"
                        "r o python e QT para desenvolver aplica\u00e7\u00f5es modernas e funcionais</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"><br /></span></p></body></html>", None))
        self.tbx_menubar.setItemText(self.tbx_menubar.indexOf(self.page_sobre), QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_toggle.setText("")
        self.lbl_head.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Sistema de cadastro de empresas</span></p></body></html>", None))
        self.txt_empresascadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">EMPRESAS</span></p></body></html>", None))
        self.txt_email.setText("")
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_municipio.setText("")
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_telefone.setText("")
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_complemento.setText("")
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.txt_cnpj.setText("")
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_bairro.setText("")
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_cep.setText("")
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_nmempresarial.setText("")
        self.txt_nmempresarial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.txt_uf.setText("")
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"uf", None))
        self.txt_numero.setText("")
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_logradouro.setText("")
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.tabw_cadastro.setTabText(self.tabw_cadastro.indexOf(self.tab_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.tbl_head.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#fdfdfd;\">Empresas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tbwl_empresas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tbwl_empresas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tbwl_empresas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tbwl_empresas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.tbwl_empresas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLENETO", None));
        ___qtablewidgetitem5 = self.tbwl_empresas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tbwl_empresas.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.tbwl_empresas.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tbwl_empresas.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tbwl_empresas.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TEL", None));
        ___qtablewidgetitem10 = self.tbwl_empresas.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_gerarexecel.setText(QCoreApplication.translate("MainWindow", u"Gerar Execel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabw_cadastro.setTabText(self.tabw_cadastro.indexOf(self.tab_empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/img/images/images/PyBlackWolf (4).png\"/></p></body></html>", None))
        self.txt_contatos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">CONTATOS</span></p></body></html>", None))
        self.lbl_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; vertical-align:super;\">(11)962800310</span></p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">lucaslobopereira@outlook.com</span></p></body></html>", None))
        self.lbl_in.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://www.linkedin.com/in/lucas-lobo-a4bb23125/\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">Perfil Lucas Lobo</span></a></p></body></html>", None))
        self.lbl_footer.setText(QCoreApplication.translate("MainWindow", u"By: Lucas Lobo Pereira", None))
    # retranslateUi

