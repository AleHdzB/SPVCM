# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 676)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FrameSup = QFrame(self.centralwidget)
        self.FrameSup.setObjectName(u"FrameSup")
        self.FrameSup.setMinimumSize(QSize(0, 100))
        self.FrameSup.setMaximumSize(QSize(16777215, 100))
        self.FrameSup.setStyleSheet(u"background-color:rgb(0, 139, 0);")
        self.FrameSup.setFrameShape(QFrame.StyledPanel)
        self.FrameSup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FrameSup)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButtonHamburguesa = QPushButton(self.FrameSup)
        self.pushButtonHamburguesa.setObjectName(u"pushButtonHamburguesa")
        self.pushButtonHamburguesa.setMinimumSize(QSize(90, 90))
        self.pushButtonHamburguesa.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(221, 37, 13);\n"
"\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:2px solid #000000;\n"
"\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"Iconos/hamburguesa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHamburguesa.setIcon(icon)
        self.pushButtonHamburguesa.setIconSize(QSize(36, 32))

        self.horizontalLayout_3.addWidget(self.pushButtonHamburguesa)

        self.pushButtonComandas = QPushButton(self.FrameSup)
        self.pushButtonComandas.setObjectName(u"pushButtonComandas")
        self.pushButtonComandas.setMinimumSize(QSize(90, 90))
        self.pushButtonComandas.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0, 0, 0,0%);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Iconos/Comanda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonComandas.setIcon(icon1)
        self.pushButtonComandas.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.pushButtonComandas)

        self.pushButtonPlatillos = QPushButton(self.FrameSup)
        self.pushButtonPlatillos.setObjectName(u"pushButtonPlatillos")
        self.pushButtonPlatillos.setMinimumSize(QSize(90, 90))
        self.pushButtonPlatillos.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0, 0, 0,0%);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Iconos/platillo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonPlatillos.setIcon(icon2)
        self.pushButtonPlatillos.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.pushButtonPlatillos)

        self.pushButtonCompras = QPushButton(self.FrameSup)
        self.pushButtonCompras.setObjectName(u"pushButtonCompras")
        self.pushButtonCompras.setMinimumSize(QSize(90, 90))
        self.pushButtonCompras.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0, 0, 0,0%);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"Iconos/compra.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCompras.setIcon(icon3)
        self.pushButtonCompras.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.pushButtonCompras)

        self.pushButtonInsumos = QPushButton(self.FrameSup)
        self.pushButtonInsumos.setObjectName(u"pushButtonInsumos")
        self.pushButtonInsumos.setMinimumSize(QSize(90, 90))
        self.pushButtonInsumos.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0, 0, 0,0%);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"Iconos/Insumo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonInsumos.setIcon(icon4)
        self.pushButtonInsumos.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.pushButtonInsumos)

        self.pushButtonEmpleados = QPushButton(self.FrameSup)
        self.pushButtonEmpleados.setObjectName(u"pushButtonEmpleados")
        self.pushButtonEmpleados.setMinimumSize(QSize(90, 90))
        self.pushButtonEmpleados.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0, 0, 0,0%);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"Iconos/Empleado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonEmpleados.setIcon(icon5)
        self.pushButtonEmpleados.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.pushButtonEmpleados)

        self.pushButtonProveedores = QPushButton(self.FrameSup)
        self.pushButtonProveedores.setObjectName(u"pushButtonProveedores")
        self.pushButtonProveedores.setMinimumSize(QSize(90, 90))
        self.pushButtonProveedores.setStyleSheet(u"QPushButton{\n"
"background-color:rgba(0, 0, 0,0%);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"Iconos/Proveedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonProveedores.setIcon(icon6)
        self.pushButtonProveedores.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.pushButtonProveedores)


        self.gridLayout_3.addWidget(self.FrameSup, 0, 0, 1, 1)

        self.FrameInf = QFrame(self.centralwidget)
        self.FrameInf.setObjectName(u"FrameInf")
        self.FrameInf.setStyleSheet(u"")
        self.FrameInf.setFrameShape(QFrame.StyledPanel)
        self.FrameInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FrameInf)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Paginas = QFrame(self.FrameInf)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setStyleSheet(u"")
        self.Paginas.setFrameShape(QFrame.StyledPanel)
        self.Paginas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Paginas)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Paginas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.Inicio = QWidget()
        self.Inicio.setObjectName(u"Inicio")
        self.gridLayout = QGridLayout(self.Inicio)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.Fondo = QLabel(self.Inicio)
        self.Fondo.setObjectName(u"Fondo")
        self.Fondo.setPixmap(QPixmap(u"Iconos/puntoventa.png"))
        self.Fondo.setScaledContents(True)

        self.gridLayout.addWidget(self.Fondo, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(76, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(77, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 151, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.stackedWidget.addWidget(self.Inicio)
        self.Comandas = QWidget()
        self.Comandas.setObjectName(u"Comandas")
        self.Comandas.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.Comandas)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tab_Comandas = QTabWidget(self.Comandas)
        self.tab_Comandas.setObjectName(u"tab_Comandas")
        self.tab_Comandas.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"")
        self.RegistrarComanda = QWidget()
        self.RegistrarComanda.setObjectName(u"RegistrarComanda")
        self.RegistrarComanda.setStyleSheet(u"")
        self.gridLayout_32 = QGridLayout(self.RegistrarComanda)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.comboBox_Estatus_Comanda = QComboBox(self.RegistrarComanda)
        self.comboBox_Estatus_Comanda.addItem("")
        self.comboBox_Estatus_Comanda.addItem("")
        self.comboBox_Estatus_Comanda.setObjectName(u"comboBox_Estatus_Comanda")

        self.gridLayout_32.addWidget(self.comboBox_Estatus_Comanda, 2, 2, 1, 1)

        self.label_ID_4 = QLabel(self.RegistrarComanda)
        self.label_ID_4.setObjectName(u"label_ID_4")
        self.label_ID_4.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_32.addWidget(self.label_ID_4, 1, 1, 1, 1)

        self.ID_Comanda = QLabel(self.RegistrarComanda)
        self.ID_Comanda.setObjectName(u"ID_Comanda")
        self.ID_Comanda.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_32.addWidget(self.ID_Comanda, 1, 2, 1, 1)

        self.label_109 = QLabel(self.RegistrarComanda)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_32.addWidget(self.label_109, 2, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.RegistrarComanda)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_21 = QGridLayout(self.groupBox_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.Label_Descripcion_Platillo_Comanda = QLabel(self.groupBox_6)
        self.Label_Descripcion_Platillo_Comanda.setObjectName(u"Label_Descripcion_Platillo_Comanda")
        self.Label_Descripcion_Platillo_Comanda.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_21.addWidget(self.Label_Descripcion_Platillo_Comanda, 4, 1, 1, 1)

        self.pushButton_Agregar_Platillos_Comanda = QPushButton(self.groupBox_6)
        self.pushButton_Agregar_Platillos_Comanda.setObjectName(u"pushButton_Agregar_Platillos_Comanda")

        self.gridLayout_21.addWidget(self.pushButton_Agregar_Platillos_Comanda, 2, 4, 1, 1)

        self.pushButton_Registrar_Comanda = QPushButton(self.groupBox_6)
        self.pushButton_Registrar_Comanda.setObjectName(u"pushButton_Registrar_Comanda")

        self.gridLayout_21.addWidget(self.pushButton_Registrar_Comanda, 6, 2, 1, 1)

        self.Label_Precio_Platillo_Comanda = QLabel(self.groupBox_6)
        self.Label_Precio_Platillo_Comanda.setObjectName(u"Label_Precio_Platillo_Comanda")
        self.Label_Precio_Platillo_Comanda.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_21.addWidget(self.Label_Precio_Platillo_Comanda, 3, 1, 1, 1)

        self.pushButton_Buscar_Platillos_Comanda = QPushButton(self.groupBox_6)
        self.pushButton_Buscar_Platillos_Comanda.setObjectName(u"pushButton_Buscar_Platillos_Comanda")

        self.gridLayout_21.addWidget(self.pushButton_Buscar_Platillos_Comanda, 0, 4, 1, 1)

        self.lineEdit_ID_Platillo = QLineEdit(self.groupBox_6)
        self.lineEdit_ID_Platillo.setObjectName(u"lineEdit_ID_Platillo")

        self.gridLayout_21.addWidget(self.lineEdit_ID_Platillo, 0, 1, 1, 3)

        self.label_ID_14 = QLabel(self.groupBox_6)
        self.label_ID_14.setObjectName(u"label_ID_14")
        self.label_ID_14.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_21.addWidget(self.label_ID_14, 4, 0, 1, 1)

        self.spinBox_Cantidad_Platillo = QSpinBox(self.groupBox_6)
        self.spinBox_Cantidad_Platillo.setObjectName(u"spinBox_Cantidad_Platillo")

        self.gridLayout_21.addWidget(self.spinBox_Cantidad_Platillo, 1, 1, 1, 1)

        self.label_108 = QLabel(self.groupBox_6)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_21.addWidget(self.label_108, 0, 0, 1, 1)

        self.Label_Nombre_Platillo_Comanda = QLabel(self.groupBox_6)
        self.Label_Nombre_Platillo_Comanda.setObjectName(u"Label_Nombre_Platillo_Comanda")
        self.Label_Nombre_Platillo_Comanda.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_21.addWidget(self.Label_Nombre_Platillo_Comanda, 2, 1, 1, 1)

        self.label_ID_12 = QLabel(self.groupBox_6)
        self.label_ID_12.setObjectName(u"label_ID_12")
        self.label_ID_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_21.addWidget(self.label_ID_12, 2, 0, 1, 1)

        self.tabla_Platillos = QTableWidget(self.groupBox_6)
        self.tabla_Platillos.setObjectName(u"tabla_Platillos")

        self.gridLayout_21.addWidget(self.tabla_Platillos, 5, 0, 1, 5)

        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")

        self.gridLayout_21.addWidget(self.label, 1, 0, 1, 1)

        self.label_ID_13 = QLabel(self.groupBox_6)
        self.label_ID_13.setObjectName(u"label_ID_13")
        self.label_ID_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_21.addWidget(self.label_ID_13, 3, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_6, 3, 1, 2, 2)

        self.groupBox_5 = QGroupBox(self.RegistrarComanda)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_18 = QGridLayout(self.groupBox_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_ID_5 = QLabel(self.groupBox_5)
        self.label_ID_5.setObjectName(u"label_ID_5")
        self.label_ID_5.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_18.addWidget(self.label_ID_5, 0, 0, 1, 1)

        self.Subtotal = QLabel(self.groupBox_5)
        self.Subtotal.setObjectName(u"Subtotal")
        self.Subtotal.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_18.addWidget(self.Subtotal, 0, 1, 1, 1)

        self.Total = QLabel(self.groupBox_5)
        self.Total.setObjectName(u"Total")
        self.Total.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_18.addWidget(self.Total, 2, 1, 1, 1)

        self.IVA = QLabel(self.groupBox_5)
        self.IVA.setObjectName(u"IVA")
        self.IVA.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_18.addWidget(self.IVA, 1, 1, 1, 1)

        self.label_ID_11 = QLabel(self.groupBox_5)
        self.label_ID_11.setObjectName(u"label_ID_11")
        self.label_ID_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_18.addWidget(self.label_ID_11, 2, 0, 1, 1)

        self.label_ID_10 = QLabel(self.groupBox_5)
        self.label_ID_10.setObjectName(u"label_ID_10")
        self.label_ID_10.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_18.addWidget(self.label_ID_10, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_5, 4, 3, 1, 1)

        self.fecha_comanda = QLabel(self.RegistrarComanda)
        self.fecha_comanda.setObjectName(u"fecha_comanda")
        self.fecha_comanda.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 0, 0);\n"
"")

        self.gridLayout_32.addWidget(self.fecha_comanda, 1, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 280, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_8, 3, 3, 1, 1)

        self.label_Titulo_Registrar_3 = QLabel(self.RegistrarComanda)
        self.label_Titulo_Registrar_3.setObjectName(u"label_Titulo_Registrar_3")
        self.label_Titulo_Registrar_3.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_3.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_3.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_3.setLineWidth(-1)
        self.label_Titulo_Registrar_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.label_Titulo_Registrar_3, 0, 2, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_45, 2, 0, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_46, 2, 3, 1, 1)

        self.tab_Comandas.addTab(self.RegistrarComanda, "")
        self.BuscarComanda = QWidget()
        self.BuscarComanda.setObjectName(u"BuscarComanda")
        self.gridLayout_23 = QGridLayout(self.BuscarComanda)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalSpacer_33 = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_33, 0, 0, 1, 1)

        self.label_Titulo_Registrar_5 = QLabel(self.BuscarComanda)
        self.label_Titulo_Registrar_5.setObjectName(u"label_Titulo_Registrar_5")
        self.label_Titulo_Registrar_5.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_5.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_5.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_5.setLineWidth(-1)
        self.label_Titulo_Registrar_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_Titulo_Registrar_5, 0, 3, 1, 3)

        self.horizontalSpacer_36 = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_36, 3, 6, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 226, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_11, 4, 6, 1, 1)

        self.Label_Estatus_Comanda_Buscar = QLabel(self.BuscarComanda)
        self.Label_Estatus_Comanda_Buscar.setObjectName(u"Label_Estatus_Comanda_Buscar")
        self.Label_Estatus_Comanda_Buscar.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout_23.addWidget(self.Label_Estatus_Comanda_Buscar, 2, 4, 1, 1)

        self.label_ID_19 = QLabel(self.BuscarComanda)
        self.label_ID_19.setObjectName(u"label_ID_19")
        self.label_ID_19.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_23.addWidget(self.label_ID_19, 1, 3, 1, 1)

        self.label_111 = QLabel(self.BuscarComanda)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_23.addWidget(self.label_111, 2, 3, 1, 1)

        self.groupBox_7 = QGroupBox(self.BuscarComanda)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_22 = QGridLayout(self.groupBox_7)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_ID_15 = QLabel(self.groupBox_7)
        self.label_ID_15.setObjectName(u"label_ID_15")
        self.label_ID_15.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_22.addWidget(self.label_ID_15, 0, 0, 1, 1)

        self.Subtotal_2 = QLabel(self.groupBox_7)
        self.Subtotal_2.setObjectName(u"Subtotal_2")
        self.Subtotal_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_22.addWidget(self.Subtotal_2, 0, 1, 1, 1)

        self.Total_2 = QLabel(self.groupBox_7)
        self.Total_2.setObjectName(u"Total_2")
        self.Total_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_22.addWidget(self.Total_2, 2, 1, 1, 1)

        self.IVA_2 = QLabel(self.groupBox_7)
        self.IVA_2.setObjectName(u"IVA_2")
        self.IVA_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_22.addWidget(self.IVA_2, 1, 1, 1, 1)

        self.label_ID_16 = QLabel(self.groupBox_7)
        self.label_ID_16.setObjectName(u"label_ID_16")
        self.label_ID_16.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_22.addWidget(self.label_ID_16, 2, 0, 1, 1)

        self.label_ID_17 = QLabel(self.groupBox_7)
        self.label_ID_17.setObjectName(u"label_ID_17")
        self.label_ID_17.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_22.addWidget(self.label_ID_17, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.groupBox_7, 5, 6, 2, 1)

        self.groupBox_8 = QGroupBox(self.BuscarComanda)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_16 = QGridLayout(self.groupBox_8)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.tabla_Buscar_Platillos = QTableWidget(self.groupBox_8)
        self.tabla_Buscar_Platillos.setObjectName(u"tabla_Buscar_Platillos")

        self.gridLayout_16.addWidget(self.tabla_Buscar_Platillos, 0, 0, 1, 2)


        self.gridLayout_23.addWidget(self.groupBox_8, 3, 1, 4, 5)

        self.pushButton_Buscar_Comanda = QPushButton(self.BuscarComanda)
        self.pushButton_Buscar_Comanda.setObjectName(u"pushButton_Buscar_Comanda")

        self.gridLayout_23.addWidget(self.pushButton_Buscar_Comanda, 1, 5, 1, 1)

        self.lineEdit_ID_Buscar_Comanda = QLineEdit(self.BuscarComanda)
        self.lineEdit_ID_Buscar_Comanda.setObjectName(u"lineEdit_ID_Buscar_Comanda")
        self.lineEdit_ID_Buscar_Comanda.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.lineEdit_ID_Buscar_Comanda, 1, 4, 1, 1)

        self.fecha_buscar_comadna = QLabel(self.BuscarComanda)
        self.fecha_buscar_comadna.setObjectName(u"fecha_buscar_comadna")
        self.fecha_buscar_comadna.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.fecha_buscar_comadna, 1, 6, 1, 1)

        self.tab_Comandas.addTab(self.BuscarComanda, "")
        self.ConsultarComanda = QWidget()
        self.ConsultarComanda.setObjectName(u"ConsultarComanda")
        self.gridLayout_24 = QGridLayout(self.ConsultarComanda)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.tab_Comandas.addTab(self.ConsultarComanda, "")
        self.ModificarComanda = QWidget()
        self.ModificarComanda.setObjectName(u"ModificarComanda")
        self.gridLayout_27 = QGridLayout(self.ModificarComanda)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_Titulo_Registrar_6 = QLabel(self.ModificarComanda)
        self.label_Titulo_Registrar_6.setObjectName(u"label_Titulo_Registrar_6")
        self.label_Titulo_Registrar_6.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_6.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_6.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_6.setLineWidth(-1)
        self.label_Titulo_Registrar_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_27.addWidget(self.label_Titulo_Registrar_6, 0, 1, 1, 4)

        self.label_ID_20 = QLabel(self.ModificarComanda)
        self.label_ID_20.setObjectName(u"label_ID_20")
        self.label_ID_20.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_27.addWidget(self.label_ID_20, 1, 1, 1, 1)

        self.pushButton_Modificar_Comanda = QPushButton(self.ModificarComanda)
        self.pushButton_Modificar_Comanda.setObjectName(u"pushButton_Modificar_Comanda")

        self.gridLayout_27.addWidget(self.pushButton_Modificar_Comanda, 6, 2, 1, 1)

        self.label_112 = QLabel(self.ModificarComanda)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_27.addWidget(self.label_112, 2, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.ModificarComanda)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_25 = QGridLayout(self.groupBox_9)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_ID_18 = QLabel(self.groupBox_9)
        self.label_ID_18.setObjectName(u"label_ID_18")
        self.label_ID_18.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_25.addWidget(self.label_ID_18, 0, 0, 1, 1)

        self.Subtotal_3 = QLabel(self.groupBox_9)
        self.Subtotal_3.setObjectName(u"Subtotal_3")
        self.Subtotal_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_25.addWidget(self.Subtotal_3, 0, 1, 1, 1)

        self.Total_3 = QLabel(self.groupBox_9)
        self.Total_3.setObjectName(u"Total_3")
        self.Total_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_25.addWidget(self.Total_3, 2, 1, 1, 1)

        self.IVA_3 = QLabel(self.groupBox_9)
        self.IVA_3.setObjectName(u"IVA_3")
        self.IVA_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_25.addWidget(self.IVA_3, 1, 1, 1, 1)

        self.label_ID_21 = QLabel(self.groupBox_9)
        self.label_ID_21.setObjectName(u"label_ID_21")
        self.label_ID_21.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_25.addWidget(self.label_ID_21, 2, 0, 1, 1)

        self.label_ID_22 = QLabel(self.groupBox_9)
        self.label_ID_22.setObjectName(u"label_ID_22")
        self.label_ID_22.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_25.addWidget(self.label_ID_22, 1, 0, 1, 1)


        self.gridLayout_27.addWidget(self.groupBox_9, 5, 4, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(192, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_34, 0, 0, 1, 1)

        self.lineEdit_ID_Comand_Modificar = QLineEdit(self.ModificarComanda)
        self.lineEdit_ID_Comand_Modificar.setObjectName(u"lineEdit_ID_Comand_Modificar")
        self.lineEdit_ID_Comand_Modificar.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.lineEdit_ID_Comand_Modificar, 1, 2, 1, 1)

        self.comboBox_Estatus_Comanda_2 = QComboBox(self.ModificarComanda)
        self.comboBox_Estatus_Comanda_2.addItem("")
        self.comboBox_Estatus_Comanda_2.addItem("")
        self.comboBox_Estatus_Comanda_2.setObjectName(u"comboBox_Estatus_Comanda_2")

        self.gridLayout_27.addWidget(self.comboBox_Estatus_Comanda_2, 2, 2, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(192, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_37, 3, 4, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 193, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_12, 4, 4, 1, 1)

        self.pushButton_Buscar_Comanda_Modificar = QPushButton(self.ModificarComanda)
        self.pushButton_Buscar_Comanda_Modificar.setObjectName(u"pushButton_Buscar_Comanda_Modificar")

        self.gridLayout_27.addWidget(self.pushButton_Buscar_Comanda_Modificar, 1, 3, 1, 1)

        self.label_6 = QLabel(self.ModificarComanda)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_27.addWidget(self.label_6, 1, 4, 1, 1)

        self.groupBox_10 = QGroupBox(self.ModificarComanda)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_26 = QGridLayout(self.groupBox_10)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.tabla_Platillos_2 = QTableWidget(self.groupBox_10)
        self.tabla_Platillos_2.setObjectName(u"tabla_Platillos_2")

        self.gridLayout_26.addWidget(self.tabla_Platillos_2, 0, 0, 1, 2)


        self.gridLayout_27.addWidget(self.groupBox_10, 3, 1, 3, 3)

        self.tab_Comandas.addTab(self.ModificarComanda, "")

        self.horizontalLayout_6.addWidget(self.tab_Comandas)

        self.stackedWidget.addWidget(self.Comandas)
        self.Platillos = QWidget()
        self.Platillos.setObjectName(u"Platillos")
        self.verticalLayout = QVBoxLayout(self.Platillos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_Platillos = QTabWidget(self.Platillos)
        self.tab_Platillos.setObjectName(u"tab_Platillos")
        self.tab_Platillos.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.RegistrarPlatillo = QWidget()
        self.RegistrarPlatillo.setObjectName(u"RegistrarPlatillo")
        self.RegistrarPlatillo.setStyleSheet(u"")
        self.gridLayout_20 = QGridLayout(self.RegistrarPlatillo)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.comboBox_Estatus_Platillo = QComboBox(self.RegistrarPlatillo)
        self.comboBox_Estatus_Platillo.addItem("")
        self.comboBox_Estatus_Platillo.addItem("")
        self.comboBox_Estatus_Platillo.setObjectName(u"comboBox_Estatus_Platillo")

        self.gridLayout_20.addWidget(self.comboBox_Estatus_Platillo, 5, 3, 1, 2)

        self.label_Existencia_3 = QLabel(self.RegistrarPlatillo)
        self.label_Existencia_3.setObjectName(u"label_Existencia_3")
        self.label_Existencia_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_20.addWidget(self.label_Existencia_3, 3, 2, 1, 1)

        self.label_Titulo_Registrar_2 = QLabel(self.RegistrarPlatillo)
        self.label_Titulo_Registrar_2.setObjectName(u"label_Titulo_Registrar_2")
        self.label_Titulo_Registrar_2.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_2.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_2.setStyleSheet(u"font: 70 20pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_2.setLineWidth(-1)
        self.label_Titulo_Registrar_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.label_Titulo_Registrar_2, 0, 3, 1, 2)

        self.lineEdit_Descripcion_Platillo = QLineEdit(self.RegistrarPlatillo)
        self.lineEdit_Descripcion_Platillo.setObjectName(u"lineEdit_Descripcion_Platillo")

        self.gridLayout_20.addWidget(self.lineEdit_Descripcion_Platillo, 4, 3, 1, 2)

        self.ID_Platillo = QLabel(self.RegistrarPlatillo)
        self.ID_Platillo.setObjectName(u"ID_Platillo")
        self.ID_Platillo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_20.addWidget(self.ID_Platillo, 1, 3, 1, 2)

        self.label_106 = QLabel(self.RegistrarPlatillo)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_20.addWidget(self.label_106, 5, 2, 1, 1)

        self.label_ID_3 = QLabel(self.RegistrarPlatillo)
        self.label_ID_3.setObjectName(u"label_ID_3")
        self.label_ID_3.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_20.addWidget(self.label_ID_3, 1, 2, 1, 1)

        self.label_Descripcion_3 = QLabel(self.RegistrarPlatillo)
        self.label_Descripcion_3.setObjectName(u"label_Descripcion_3")
        self.label_Descripcion_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_20.addWidget(self.label_Descripcion_3, 4, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_9, 0, 5, 1, 1)

        self.groupBox = QGroupBox(self.RegistrarPlatillo)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_107 = QLabel(self.groupBox)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_5.addWidget(self.label_107, 0, 0, 1, 1)

        self.lineEdit_ID_Insumos_Platillo = QLineEdit(self.groupBox)
        self.lineEdit_ID_Insumos_Platillo.setObjectName(u"lineEdit_ID_Insumos_Platillo")

        self.gridLayout_5.addWidget(self.lineEdit_ID_Insumos_Platillo, 0, 1, 1, 2)

        self.pushButton_Buscar_Insumos_ID = QPushButton(self.groupBox)
        self.pushButton_Buscar_Insumos_ID.setObjectName(u"pushButton_Buscar_Insumos_ID")

        self.gridLayout_5.addWidget(self.pushButton_Buscar_Insumos_ID, 0, 3, 1, 1)

        self.label_ID_7 = QLabel(self.groupBox)
        self.label_ID_7.setObjectName(u"label_ID_7")
        self.label_ID_7.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_5.addWidget(self.label_ID_7, 1, 0, 1, 1)

        self.Label_Nombre_Insumo = QLabel(self.groupBox)
        self.Label_Nombre_Insumo.setObjectName(u"Label_Nombre_Insumo")
        self.Label_Nombre_Insumo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(1, 1, 1);")

        self.gridLayout_5.addWidget(self.Label_Nombre_Insumo, 1, 1, 1, 1)

        self.pushButton_Agregar_Insumo = QPushButton(self.groupBox)
        self.pushButton_Agregar_Insumo.setObjectName(u"pushButton_Agregar_Insumo")

        self.gridLayout_5.addWidget(self.pushButton_Agregar_Insumo, 1, 3, 1, 1)

        self.label_ID_8 = QLabel(self.groupBox)
        self.label_ID_8.setObjectName(u"label_ID_8")
        self.label_ID_8.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_5.addWidget(self.label_ID_8, 2, 0, 1, 1)

        self.Label_Descripcion_Insumo = QLabel(self.groupBox)
        self.Label_Descripcion_Insumo.setObjectName(u"Label_Descripcion_Insumo")
        self.Label_Descripcion_Insumo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(1,	1, 1);")

        self.gridLayout_5.addWidget(self.Label_Descripcion_Insumo, 2, 1, 1, 1)

        self.label_ID_9 = QLabel(self.groupBox)
        self.label_ID_9.setObjectName(u"label_ID_9")
        self.label_ID_9.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_ID_9, 3, 0, 1, 1)

        self.SpinBox_Cantidad_Insumo = QDoubleSpinBox(self.groupBox)
        self.SpinBox_Cantidad_Insumo.setObjectName(u"SpinBox_Cantidad_Insumo")
        self.SpinBox_Cantidad_Insumo.setDecimals(2)
        self.SpinBox_Cantidad_Insumo.setMinimum(0.000000000000000)

        self.gridLayout_5.addWidget(self.SpinBox_Cantidad_Insumo, 3, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_29, 3, 2, 1, 2)

        self.tabla_Buscar_Insumos_Platillo = QTableWidget(self.groupBox)
        self.tabla_Buscar_Insumos_Platillo.setObjectName(u"tabla_Buscar_Insumos_Platillo")

        self.gridLayout_5.addWidget(self.tabla_Buscar_Insumos_Platillo, 4, 0, 1, 4)


        self.gridLayout_20.addWidget(self.groupBox, 6, 1, 1, 5)

        self.horizontalSpacer_32 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_32, 7, 6, 1, 1)

        self.SpinBox_Precio_Platillo = QDoubleSpinBox(self.RegistrarPlatillo)
        self.SpinBox_Precio_Platillo.setObjectName(u"SpinBox_Precio_Platillo")

        self.gridLayout_20.addWidget(self.SpinBox_Precio_Platillo, 3, 3, 1, 2)

        self.lineEdit_Nombre_Platillo = QLineEdit(self.RegistrarPlatillo)
        self.lineEdit_Nombre_Platillo.setObjectName(u"lineEdit_Nombre_Platillo")

        self.gridLayout_20.addWidget(self.lineEdit_Nombre_Platillo, 2, 3, 1, 2)

        self.horizontalSpacer_31 = QSpacerItem(138, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_31, 7, 0, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.label_Nombre_Insumo_3 = QLabel(self.RegistrarPlatillo)
        self.label_Nombre_Insumo_3.setObjectName(u"label_Nombre_Insumo_3")
        self.label_Nombre_Insumo_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_20.addWidget(self.label_Nombre_Insumo_3, 2, 2, 1, 1)

        self.pushButton_Registrar_Platillo = QPushButton(self.RegistrarPlatillo)
        self.pushButton_Registrar_Platillo.setObjectName(u"pushButton_Registrar_Platillo")

        self.gridLayout_20.addWidget(self.pushButton_Registrar_Platillo, 7, 2, 1, 4)

        self.tab_Platillos.addTab(self.RegistrarPlatillo, "")
        self.BuscarPlatillo = QWidget()
        self.BuscarPlatillo.setObjectName(u"BuscarPlatillo")
        self.gridLayout_29 = QGridLayout(self.BuscarPlatillo)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.label_Titulo_Registrar_7 = QLabel(self.BuscarPlatillo)
        self.label_Titulo_Registrar_7.setObjectName(u"label_Titulo_Registrar_7")
        self.label_Titulo_Registrar_7.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_7.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_7.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_7.setLineWidth(-1)
        self.label_Titulo_Registrar_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.label_Titulo_Registrar_7, 0, 3, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_10, 0, 5, 1, 1)

        self.label_ID_26 = QLabel(self.BuscarPlatillo)
        self.label_ID_26.setObjectName(u"label_ID_26")
        self.label_ID_26.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_29.addWidget(self.label_ID_26, 1, 1, 1, 1)

        self.label_Nombre_Insumo_5 = QLabel(self.BuscarPlatillo)
        self.label_Nombre_Insumo_5.setObjectName(u"label_Nombre_Insumo_5")
        self.label_Nombre_Insumo_5.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_29.addWidget(self.label_Nombre_Insumo_5, 2, 1, 1, 2)

        self.Nombre_Platillo = QLabel(self.BuscarPlatillo)
        self.Nombre_Platillo.setObjectName(u"Nombre_Platillo")
        self.Nombre_Platillo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout_29.addWidget(self.Nombre_Platillo, 2, 3, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_30, 3, 0, 2, 1)

        self.label_Existencia_4 = QLabel(self.BuscarPlatillo)
        self.label_Existencia_4.setObjectName(u"label_Existencia_4")
        self.label_Existencia_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_29.addWidget(self.label_Existencia_4, 3, 1, 1, 2)

        self.Precio_Platillo = QLabel(self.BuscarPlatillo)
        self.Precio_Platillo.setObjectName(u"Precio_Platillo")
        self.Precio_Platillo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout_29.addWidget(self.Precio_Platillo, 3, 3, 1, 1)

        self.label_Descripcion_4 = QLabel(self.BuscarPlatillo)
        self.label_Descripcion_4.setObjectName(u"label_Descripcion_4")
        self.label_Descripcion_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_29.addWidget(self.label_Descripcion_4, 4, 1, 1, 2)

        self.Descripcion_Platillo = QLabel(self.BuscarPlatillo)
        self.Descripcion_Platillo.setObjectName(u"Descripcion_Platillo")
        self.Descripcion_Platillo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout_29.addWidget(self.Descripcion_Platillo, 4, 3, 1, 1)

        self.label_114 = QLabel(self.BuscarPlatillo)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_29.addWidget(self.label_114, 5, 1, 1, 2)

        self.Esatus_Platillo = QLabel(self.BuscarPlatillo)
        self.Esatus_Platillo.setObjectName(u"Esatus_Platillo")
        self.Esatus_Platillo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"")

        self.gridLayout_29.addWidget(self.Esatus_Platillo, 5, 3, 1, 1)

        self.groupBox_11 = QGroupBox(self.BuscarPlatillo)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_28 = QGridLayout(self.groupBox_11)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.tabla_Buscar_Insumos_Platillo_2 = QTableWidget(self.groupBox_11)
        self.tabla_Buscar_Insumos_Platillo_2.setObjectName(u"tabla_Buscar_Insumos_Platillo_2")

        self.gridLayout_28.addWidget(self.tabla_Buscar_Insumos_Platillo_2, 0, 0, 1, 2)


        self.gridLayout_29.addWidget(self.groupBox_11, 6, 1, 1, 5)

        self.horizontalSpacer_35 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_35, 6, 6, 1, 1)

        self.pushButton_Buscar_Platillo = QPushButton(self.BuscarPlatillo)
        self.pushButton_Buscar_Platillo.setObjectName(u"pushButton_Buscar_Platillo")

        self.gridLayout_29.addWidget(self.pushButton_Buscar_Platillo, 1, 5, 1, 1)

        self.lineEdit_ID_Buscar_Platillo = QLineEdit(self.BuscarPlatillo)
        self.lineEdit_ID_Buscar_Platillo.setObjectName(u"lineEdit_ID_Buscar_Platillo")

        self.gridLayout_29.addWidget(self.lineEdit_ID_Buscar_Platillo, 1, 2, 1, 3)

        self.tab_Platillos.addTab(self.BuscarPlatillo, "")
        self.ConsultarPlatillo = QWidget()
        self.ConsultarPlatillo.setObjectName(u"ConsultarPlatillo")
        self.gridLayout_30 = QGridLayout(self.ConsultarPlatillo)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalSpacer_39 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_39, 0, 0, 1, 1)

        self.Titulo_Consultar_Insumo_2 = QLabel(self.ConsultarPlatillo)
        self.Titulo_Consultar_Insumo_2.setObjectName(u"Titulo_Consultar_Insumo_2")
        self.Titulo_Consultar_Insumo_2.setMinimumSize(QSize(30, 30))
        self.Titulo_Consultar_Insumo_2.setMaximumSize(QSize(1500, 200))
        self.Titulo_Consultar_Insumo_2.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.Titulo_Consultar_Insumo_2.setLineWidth(-1)
        self.Titulo_Consultar_Insumo_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.Titulo_Consultar_Insumo_2, 0, 1, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(171, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_38, 0, 2, 1, 1)

        self.tabla_Consultar_Platillos = QTableWidget(self.ConsultarPlatillo)
        self.tabla_Consultar_Platillos.setObjectName(u"tabla_Consultar_Platillos")

        self.gridLayout_30.addWidget(self.tabla_Consultar_Platillos, 1, 0, 1, 3)

        self.pushButton_Mostrar_Platillos = QPushButton(self.ConsultarPlatillo)
        self.pushButton_Mostrar_Platillos.setObjectName(u"pushButton_Mostrar_Platillos")

        self.gridLayout_30.addWidget(self.pushButton_Mostrar_Platillos, 2, 1, 1, 1)

        self.tab_Platillos.addTab(self.ConsultarPlatillo, "")
        self.ModificarPlatillo = QWidget()
        self.ModificarPlatillo.setObjectName(u"ModificarPlatillo")
        self.lineEdit_Nombre_Platillo_2 = QLineEdit(self.ModificarPlatillo)
        self.lineEdit_Nombre_Platillo_2.setObjectName(u"lineEdit_Nombre_Platillo_2")
        self.lineEdit_Nombre_Platillo_2.setGeometry(QRect(309, 72, 275, 29))
        self.groupBox_12 = QGroupBox(self.ModificarPlatillo)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(194, 210, 512, 254))
        self.gridLayout_31 = QGridLayout(self.groupBox_12)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_113 = QLabel(self.groupBox_12)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_31.addWidget(self.label_113, 0, 0, 1, 1)

        self.lineEdit_ID_Insumos_Platillo_Modificar = QLineEdit(self.groupBox_12)
        self.lineEdit_ID_Insumos_Platillo_Modificar.setObjectName(u"lineEdit_ID_Insumos_Platillo_Modificar")

        self.gridLayout_31.addWidget(self.lineEdit_ID_Insumos_Platillo_Modificar, 0, 1, 1, 2)

        self.pushButton_Buscar_Insumos_Modificar = QPushButton(self.groupBox_12)
        self.pushButton_Buscar_Insumos_Modificar.setObjectName(u"pushButton_Buscar_Insumos_Modificar")

        self.gridLayout_31.addWidget(self.pushButton_Buscar_Insumos_Modificar, 0, 3, 1, 1)

        self.label_ID_23 = QLabel(self.groupBox_12)
        self.label_ID_23.setObjectName(u"label_ID_23")
        self.label_ID_23.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_31.addWidget(self.label_ID_23, 1, 0, 1, 1)

        self.Label_Nombre_Insumo_2 = QLabel(self.groupBox_12)
        self.Label_Nombre_Insumo_2.setObjectName(u"Label_Nombre_Insumo_2")
        self.Label_Nombre_Insumo_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(1, 1, 1);")

        self.gridLayout_31.addWidget(self.Label_Nombre_Insumo_2, 1, 1, 1, 1)

        self.pushButton_Agregar_Insumo_2 = QPushButton(self.groupBox_12)
        self.pushButton_Agregar_Insumo_2.setObjectName(u"pushButton_Agregar_Insumo_2")

        self.gridLayout_31.addWidget(self.pushButton_Agregar_Insumo_2, 1, 3, 1, 1)

        self.label_ID_24 = QLabel(self.groupBox_12)
        self.label_ID_24.setObjectName(u"label_ID_24")
        self.label_ID_24.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_31.addWidget(self.label_ID_24, 2, 0, 1, 1)

        self.Label_Descripcion_Insumo_2 = QLabel(self.groupBox_12)
        self.Label_Descripcion_Insumo_2.setObjectName(u"Label_Descripcion_Insumo_2")
        self.Label_Descripcion_Insumo_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(1,	1, 1);")

        self.gridLayout_31.addWidget(self.Label_Descripcion_Insumo_2, 2, 1, 1, 1)

        self.label_ID_25 = QLabel(self.groupBox_12)
        self.label_ID_25.setObjectName(u"label_ID_25")
        self.label_ID_25.setStyleSheet(u"")

        self.gridLayout_31.addWidget(self.label_ID_25, 3, 0, 1, 1)

        self.SpinBox_Cantidad_Insumo_2 = QDoubleSpinBox(self.groupBox_12)
        self.SpinBox_Cantidad_Insumo_2.setObjectName(u"SpinBox_Cantidad_Insumo_2")
        self.SpinBox_Cantidad_Insumo_2.setDecimals(2)
        self.SpinBox_Cantidad_Insumo_2.setMinimum(0.000000000000000)

        self.gridLayout_31.addWidget(self.SpinBox_Cantidad_Insumo_2, 3, 1, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_41, 3, 2, 1, 2)

        self.tabla_Modificar_Insumo_Platillo = QTableWidget(self.groupBox_12)
        self.tabla_Modificar_Insumo_Platillo.setObjectName(u"tabla_Modificar_Insumo_Platillo")

        self.gridLayout_31.addWidget(self.tabla_Modificar_Insumo_Platillo, 4, 0, 1, 4)

        self.pushButton_Quitar_Insumo = QPushButton(self.groupBox_12)
        self.pushButton_Quitar_Insumo.setObjectName(u"pushButton_Quitar_Insumo")

        self.gridLayout_31.addWidget(self.pushButton_Quitar_Insumo, 2, 3, 1, 1)

        self.label_Nombre_Insumo_6 = QLabel(self.ModificarPlatillo)
        self.label_Nombre_Insumo_6.setObjectName(u"label_Nombre_Insumo_6")
        self.label_Nombre_Insumo_6.setGeometry(QRect(200, 72, 103, 29))
        self.label_Nombre_Insumo_6.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.label_Existencia_5 = QLabel(self.ModificarPlatillo)
        self.label_Existencia_5.setObjectName(u"label_Existencia_5")
        self.label_Existencia_5.setGeometry(QRect(200, 107, 103, 27))
        self.label_Existencia_5.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_Descripcion_Platillo_2 = QLineEdit(self.ModificarPlatillo)
        self.lineEdit_Descripcion_Platillo_2.setObjectName(u"lineEdit_Descripcion_Platillo_2")
        self.lineEdit_Descripcion_Platillo_2.setGeometry(QRect(309, 140, 275, 29))
        self.comboBox_Estatus_Platillo_2 = QComboBox(self.ModificarPlatillo)
        self.comboBox_Estatus_Platillo_2.addItem("")
        self.comboBox_Estatus_Platillo_2.addItem("")
        self.comboBox_Estatus_Platillo_2.setObjectName(u"comboBox_Estatus_Platillo_2")
        self.comboBox_Estatus_Platillo_2.setGeometry(QRect(309, 175, 275, 29))
        self.label_Titulo_Registrar_8 = QLabel(self.ModificarPlatillo)
        self.label_Titulo_Registrar_8.setObjectName(u"label_Titulo_Registrar_8")
        self.label_Titulo_Registrar_8.setGeometry(QRect(309, 7, 275, 30))
        self.label_Titulo_Registrar_8.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_8.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_8.setStyleSheet(u"font: 70 20pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_8.setLineWidth(-1)
        self.label_Titulo_Registrar_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_ID_27 = QLabel(self.ModificarPlatillo)
        self.label_ID_27.setObjectName(u"label_ID_27")
        self.label_ID_27.setGeometry(QRect(200, 43, 103, 23))
        self.label_ID_27.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")
        self.label_115 = QLabel(self.ModificarPlatillo)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(200, 175, 103, 29))
        self.pushButton_Modificar_Platillo = QPushButton(self.ModificarPlatillo)
        self.pushButton_Modificar_Platillo.setObjectName(u"pushButton_Modificar_Platillo")
        self.pushButton_Modificar_Platillo.setGeometry(QRect(200, 470, 506, 31))
        self.SpinBox_Precio_Platillo_2 = QDoubleSpinBox(self.ModificarPlatillo)
        self.SpinBox_Precio_Platillo_2.setObjectName(u"SpinBox_Precio_Platillo_2")
        self.SpinBox_Precio_Platillo_2.setGeometry(QRect(309, 107, 275, 27))
        self.label_Descripcion_5 = QLabel(self.ModificarPlatillo)
        self.label_Descripcion_5.setObjectName(u"label_Descripcion_5")
        self.label_Descripcion_5.setGeometry(QRect(200, 140, 103, 29))
        self.label_Descripcion_5.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_ID_Platillo_Modificar = QLineEdit(self.ModificarPlatillo)
        self.lineEdit_ID_Platillo_Modificar.setObjectName(u"lineEdit_ID_Platillo_Modificar")
        self.lineEdit_ID_Platillo_Modificar.setGeometry(QRect(240, 40, 271, 29))
        self.pushButton_Buscar_Platillo_Modificar = QPushButton(self.ModificarPlatillo)
        self.pushButton_Buscar_Platillo_Modificar.setObjectName(u"pushButton_Buscar_Platillo_Modificar")
        self.pushButton_Buscar_Platillo_Modificar.setGeometry(QRect(510, 40, 71, 31))
        self.tab_Platillos.addTab(self.ModificarPlatillo, "")

        self.verticalLayout.addWidget(self.tab_Platillos)

        self.stackedWidget.addWidget(self.Platillos)
        self.Compras = QWidget()
        self.Compras.setObjectName(u"Compras")
        self.horizontalLayout_5 = QHBoxLayout(self.Compras)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tab_Compras = QTabWidget(self.Compras)
        self.tab_Compras.setObjectName(u"tab_Compras")
        self.tab_Compras.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.RegistrarCompra = QWidget()
        self.RegistrarCompra.setObjectName(u"RegistrarCompra")
        self.RegistrarCompra.setStyleSheet(u"")
        self.gridLayout_19 = QGridLayout(self.RegistrarCompra)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_Titulo_Registrar_4 = QLabel(self.RegistrarCompra)
        self.label_Titulo_Registrar_4.setObjectName(u"label_Titulo_Registrar_4")
        self.label_Titulo_Registrar_4.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar_4.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar_4.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar_4.setLineWidth(-1)
        self.label_Titulo_Registrar_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_Titulo_Registrar_4, 0, 1, 1, 2)

        self.fecha_compra = QLabel(self.RegistrarCompra)
        self.fecha_compra.setObjectName(u"fecha_compra")
        self.fecha_compra.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_19.addWidget(self.fecha_compra, 0, 3, 3, 2)

        self.label_ID_6 = QLabel(self.RegistrarCompra)
        self.label_ID_6.setObjectName(u"label_ID_6")
        self.label_ID_6.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_19.addWidget(self.label_ID_6, 1, 1, 1, 1)

        self.ID_Compra = QLabel(self.RegistrarCompra)
        self.ID_Compra.setObjectName(u"ID_Compra")
        self.ID_Compra.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_19.addWidget(self.ID_Compra, 1, 2, 1, 1)

        self.label_Nombre_Insumo_4 = QLabel(self.RegistrarCompra)
        self.label_Nombre_Insumo_4.setObjectName(u"label_Nombre_Insumo_4")
        self.label_Nombre_Insumo_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_19.addWidget(self.label_Nombre_Insumo_4, 2, 1, 1, 1)

        self.lineEdit_ID_Proveedor = QLineEdit(self.RegistrarCompra)
        self.lineEdit_ID_Proveedor.setObjectName(u"lineEdit_ID_Proveedor")

        self.gridLayout_19.addWidget(self.lineEdit_ID_Proveedor, 2, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_14, 3, 0, 1, 1)

        self.label_110 = QLabel(self.RegistrarCompra)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_19.addWidget(self.label_110, 4, 1, 1, 1)

        self.lineEdit_ID_Insumos_Compra = QLineEdit(self.RegistrarCompra)
        self.lineEdit_ID_Insumos_Compra.setObjectName(u"lineEdit_ID_Insumos_Compra")

        self.gridLayout_19.addWidget(self.lineEdit_ID_Insumos_Compra, 4, 2, 1, 1)

        self.pushButton_Buscar_Insumos_Compra = QPushButton(self.RegistrarCompra)
        self.pushButton_Buscar_Insumos_Compra.setObjectName(u"pushButton_Buscar_Insumos_Compra")

        self.gridLayout_19.addWidget(self.pushButton_Buscar_Insumos_Compra, 4, 3, 1, 1)

        self.tabla_Buscar_Insumos_Compra = QTableWidget(self.RegistrarCompra)
        self.tabla_Buscar_Insumos_Compra.setObjectName(u"tabla_Buscar_Insumos_Compra")

        self.gridLayout_19.addWidget(self.tabla_Buscar_Insumos_Compra, 5, 1, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_12, 5, 4, 1, 1)

        self.pushButton_Registrar_Compra = QPushButton(self.RegistrarCompra)
        self.pushButton_Registrar_Compra.setObjectName(u"pushButton_Registrar_Compra")

        self.gridLayout_19.addWidget(self.pushButton_Registrar_Compra, 6, 1, 1, 3)

        self.tab_Compras.addTab(self.RegistrarCompra, "")
        self.BuscarCompra = QWidget()
        self.BuscarCompra.setObjectName(u"BuscarCompra")
        self.gridLayout_17 = QGridLayout(self.BuscarCompra)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tab_Compras.addTab(self.BuscarCompra, "")
        self.ConsultarCompra = QWidget()
        self.ConsultarCompra.setObjectName(u"ConsultarCompra")
        self.tab_Compras.addTab(self.ConsultarCompra, "")
        self.ModificarCompra = QWidget()
        self.ModificarCompra.setObjectName(u"ModificarCompra")
        self.tab_Compras.addTab(self.ModificarCompra, "")

        self.horizontalLayout_5.addWidget(self.tab_Compras)

        self.stackedWidget.addWidget(self.Compras)
        self.Insumos = QWidget()
        self.Insumos.setObjectName(u"Insumos")
        self.gridLayout_7 = QGridLayout(self.Insumos)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tab_Insumo = QTabWidget(self.Insumos)
        self.tab_Insumo.setObjectName(u"tab_Insumo")
        self.tab_Insumo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.RegistrarInsumo = QWidget()
        self.RegistrarInsumo.setObjectName(u"RegistrarInsumo")
        self.RegistrarInsumo.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.RegistrarInsumo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBoxInsumo = QGroupBox(self.RegistrarInsumo)
        self.groupBoxInsumo.setObjectName(u"groupBoxInsumo")
        self.gridLayout_2 = QGridLayout(self.groupBoxInsumo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.lineEdit_Nombre_Insumo = QLineEdit(self.groupBoxInsumo)
        self.lineEdit_Nombre_Insumo.setObjectName(u"lineEdit_Nombre_Insumo")

        self.gridLayout_2.addWidget(self.lineEdit_Nombre_Insumo, 2, 3, 1, 1)

        self.pushButton_Registrar_Inusmo = QPushButton(self.groupBoxInsumo)
        self.pushButton_Registrar_Inusmo.setObjectName(u"pushButton_Registrar_Inusmo")

        self.gridLayout_2.addWidget(self.pushButton_Registrar_Inusmo, 5, 3, 1, 1)

        self.SpinBoxExistencia = QDoubleSpinBox(self.groupBoxInsumo)
        self.SpinBoxExistencia.setObjectName(u"SpinBoxExistencia")

        self.gridLayout_2.addWidget(self.SpinBoxExistencia, 3, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 0, 1, 1)

        self.label_Descripcion = QLabel(self.groupBoxInsumo)
        self.label_Descripcion.setObjectName(u"label_Descripcion")
        self.label_Descripcion.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_Descripcion, 4, 1, 1, 2)

        self.textEdit_Descripcion = QTextEdit(self.groupBoxInsumo)
        self.textEdit_Descripcion.setObjectName(u"textEdit_Descripcion")

        self.gridLayout_2.addWidget(self.textEdit_Descripcion, 4, 3, 1, 1)

        self.label_ID = QLabel(self.groupBoxInsumo)
        self.label_ID.setObjectName(u"label_ID")
        self.label_ID.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_2.addWidget(self.label_ID, 1, 1, 1, 1)

        self.label_Existencia = QLabel(self.groupBoxInsumo)
        self.label_Existencia.setObjectName(u"label_Existencia")
        self.label_Existencia.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_Existencia, 3, 1, 1, 2)

        self.ID_Insumo = QLabel(self.groupBoxInsumo)
        self.ID_Insumo.setObjectName(u"ID_Insumo")
        self.ID_Insumo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_2.addWidget(self.ID_Insumo, 1, 3, 1, 1)

        self.label_Nombre_Insumo = QLabel(self.groupBoxInsumo)
        self.label_Nombre_Insumo.setObjectName(u"label_Nombre_Insumo")
        self.label_Nombre_Insumo.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.label_Nombre_Insumo, 2, 1, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.label_Titulo_Registrar = QLabel(self.groupBoxInsumo)
        self.label_Titulo_Registrar.setObjectName(u"label_Titulo_Registrar")
        self.label_Titulo_Registrar.setMinimumSize(QSize(30, 30))
        self.label_Titulo_Registrar.setMaximumSize(QSize(1500, 200))
        self.label_Titulo_Registrar.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titulo_Registrar.setLineWidth(-1)
        self.label_Titulo_Registrar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_Titulo_Registrar, 0, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBoxInsumo)

        self.tab_Insumo.addTab(self.RegistrarInsumo, "")
        self.BuscarInsumo = QWidget()
        self.BuscarInsumo.setObjectName(u"BuscarInsumo")
        self.gridLayout_8 = QGridLayout(self.BuscarInsumo)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(10)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_16, 0, 4, 1, 1)

        self.pushButton_Buscar_Insumo = QPushButton(self.BuscarInsumo)
        self.pushButton_Buscar_Insumo.setObjectName(u"pushButton_Buscar_Insumo")

        self.gridLayout_8.addWidget(self.pushButton_Buscar_Insumo, 3, 4, 1, 1)

        self.label_Titutlo_Busqueda = QLabel(self.BuscarInsumo)
        self.label_Titutlo_Busqueda.setObjectName(u"label_Titutlo_Busqueda")
        self.label_Titutlo_Busqueda.setMinimumSize(QSize(30, 30))
        self.label_Titutlo_Busqueda.setMaximumSize(QSize(1500, 200))
        self.label_Titutlo_Busqueda.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_Titutlo_Busqueda.setLineWidth(-1)
        self.label_Titutlo_Busqueda.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_Titutlo_Busqueda, 0, 1, 1, 2)

        self.lineEdit_Buscar_Insumo = QLineEdit(self.BuscarInsumo)
        self.lineEdit_Buscar_Insumo.setObjectName(u"lineEdit_Buscar_Insumo")

        self.gridLayout_8.addWidget(self.lineEdit_Buscar_Insumo, 3, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.tabla_Buscar_Insumo = QTableWidget(self.BuscarInsumo)
        self.tabla_Buscar_Insumo.setObjectName(u"tabla_Buscar_Insumo")

        self.gridLayout_8.addWidget(self.tabla_Buscar_Insumo, 1, 0, 1, 5)

        self.tab_Insumo.addTab(self.BuscarInsumo, "")
        self.ConsultarInsumo = QWidget()
        self.ConsultarInsumo.setObjectName(u"ConsultarInsumo")
        self.gridLayout_9 = QGridLayout(self.ConsultarInsumo)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_18 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)

        self.Titulo_Consultar_Insumo = QLabel(self.ConsultarInsumo)
        self.Titulo_Consultar_Insumo.setObjectName(u"Titulo_Consultar_Insumo")
        self.Titulo_Consultar_Insumo.setMinimumSize(QSize(30, 30))
        self.Titulo_Consultar_Insumo.setMaximumSize(QSize(1500, 200))
        self.Titulo_Consultar_Insumo.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.Titulo_Consultar_Insumo.setLineWidth(-1)
        self.Titulo_Consultar_Insumo.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Titulo_Consultar_Insumo, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.tabla_Consultar_Insumo = QTableWidget(self.ConsultarInsumo)
        self.tabla_Consultar_Insumo.setObjectName(u"tabla_Consultar_Insumo")

        self.gridLayout_9.addWidget(self.tabla_Consultar_Insumo, 1, 0, 1, 3)

        self.pushButton_Mostrar_Insumos = QPushButton(self.ConsultarInsumo)
        self.pushButton_Mostrar_Insumos.setObjectName(u"pushButton_Mostrar_Insumos")

        self.gridLayout_9.addWidget(self.pushButton_Mostrar_Insumos, 2, 1, 1, 1)

        self.tab_Insumo.addTab(self.ConsultarInsumo, "")
        self.ModificarInsumo = QWidget()
        self.ModificarInsumo.setObjectName(u"ModificarInsumo")
        self.gridLayout_11 = QGridLayout(self.ModificarInsumo)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_4 = QGroupBox(self.ModificarInsumo)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(10)
        self.label_Nombre_Insumo_2 = QLabel(self.groupBox_4)
        self.label_Nombre_Insumo_2.setObjectName(u"label_Nombre_Insumo_2")
        self.label_Nombre_Insumo_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_10.addWidget(self.label_Nombre_Insumo_2, 4, 1, 1, 2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_19, 5, 0, 1, 1)

        self.label_ID_2 = QLabel(self.groupBox_4)
        self.label_ID_2.setObjectName(u"label_ID_2")
        self.label_ID_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_10.addWidget(self.label_ID_2, 3, 1, 1, 1)

        self.SpinBox_Existencia_2 = QDoubleSpinBox(self.groupBox_4)
        self.SpinBox_Existencia_2.setObjectName(u"SpinBox_Existencia_2")

        self.gridLayout_10.addWidget(self.SpinBox_Existencia_2, 5, 3, 1, 1)

        self.textEdit_Descripcion_2 = QTextEdit(self.groupBox_4)
        self.textEdit_Descripcion_2.setObjectName(u"textEdit_Descripcion_2")

        self.gridLayout_10.addWidget(self.textEdit_Descripcion_2, 6, 3, 1, 1)

        self.pushButton_Buscar_Insum_2 = QPushButton(self.groupBox_4)
        self.pushButton_Buscar_Insum_2.setObjectName(u"pushButton_Buscar_Insum_2")

        self.gridLayout_10.addWidget(self.pushButton_Buscar_Insum_2, 1, 1, 1, 1)

        self.lineEdit_Buscar_Insumo_5 = QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar_Insumo_5.setObjectName(u"lineEdit_Buscar_Insumo_5")

        self.gridLayout_10.addWidget(self.lineEdit_Buscar_Insumo_5, 1, 2, 1, 2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_20, 0, 4, 1, 1)

        self.ID_Modificar_Insumo = QLabel(self.groupBox_4)
        self.ID_Modificar_Insumo.setObjectName(u"ID_Modificar_Insumo")
        self.ID_Modificar_Insumo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_10.addWidget(self.ID_Modificar_Insumo, 3, 3, 1, 1)

        self.lineEdit_Nombre_Insumo_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_Nombre_Insumo_2.setObjectName(u"lineEdit_Nombre_Insumo_2")

        self.gridLayout_10.addWidget(self.lineEdit_Nombre_Insumo_2, 4, 3, 1, 1)

        self.label_Descripcion_2 = QLabel(self.groupBox_4)
        self.label_Descripcion_2.setObjectName(u"label_Descripcion_2")
        self.label_Descripcion_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_10.addWidget(self.label_Descripcion_2, 6, 1, 1, 2)

        self.pushButton_Modificar_Inusmo = QPushButton(self.groupBox_4)
        self.pushButton_Modificar_Inusmo.setObjectName(u"pushButton_Modificar_Inusmo")

        self.gridLayout_10.addWidget(self.pushButton_Modificar_Inusmo, 7, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(1500, 200))
        self.label_2.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_2.setLineWidth(-1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_Existencia_2 = QLabel(self.groupBox_4)
        self.label_Existencia_2.setObjectName(u"label_Existencia_2")
        self.label_Existencia_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_10.addWidget(self.label_Existencia_2, 5, 1, 1, 2)


        self.gridLayout_11.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tab_Insumo.addTab(self.ModificarInsumo, "")

        self.gridLayout_7.addWidget(self.tab_Insumo, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Insumos)
        self.Empleados = QWidget()
        self.Empleados.setObjectName(u"Empleados")
        self.verticalLayout_4 = QVBoxLayout(self.Empleados)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tab_Empleados = QTabWidget(self.Empleados)
        self.tab_Empleados.setObjectName(u"tab_Empleados")
        self.tab_Empleados.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.RegistrarEmpleado = QWidget()
        self.RegistrarEmpleado.setObjectName(u"RegistrarEmpleado")
        self.RegistrarEmpleado.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.RegistrarEmpleado)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_2 = QGroupBox(self.RegistrarEmpleado)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.label_18, 3, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_4.addWidget(self.label_17, 1, 1, 1, 1)

        self.comboBox_Cargo_Empleado = QComboBox(self.groupBox_2)
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.setObjectName(u"comboBox_Cargo_Empleado")

        self.gridLayout_4.addWidget(self.comboBox_Cargo_Empleado, 3, 3, 1, 1)

        self.lineEdit_Nombre_Empleado = QLineEdit(self.groupBox_2)
        self.lineEdit_Nombre_Empleado.setObjectName(u"lineEdit_Nombre_Empleado")

        self.gridLayout_4.addWidget(self.lineEdit_Nombre_Empleado, 2, 3, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.label_16, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.lineEdit_Telefono_Empleado = QLineEdit(self.groupBox_2)
        self.lineEdit_Telefono_Empleado.setObjectName(u"lineEdit_Telefono_Empleado")

        self.gridLayout_4.addWidget(self.lineEdit_Telefono_Empleado, 5, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 30))
        self.label_20.setMaximumSize(QSize(1500, 200))
        self.label_20.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_20.setLineWidth(-1)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_20, 0, 3, 1, 1)

        self.pushButton_Registrar_Empleado = QPushButton(self.groupBox_2)
        self.pushButton_Registrar_Empleado.setObjectName(u"pushButton_Registrar_Empleado")

        self.gridLayout_4.addWidget(self.pushButton_Registrar_Empleado, 6, 3, 1, 1)

        self.comboBox_Estatus_Empleado = QComboBox(self.groupBox_2)
        self.comboBox_Estatus_Empleado.addItem("")
        self.comboBox_Estatus_Empleado.addItem("")
        self.comboBox_Estatus_Empleado.setObjectName(u"comboBox_Estatus_Empleado")

        self.gridLayout_4.addWidget(self.comboBox_Estatus_Empleado, 4, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 4, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.label_19, 2, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 7, 3, 1, 1)

        self.ID_Empleado = QLabel(self.groupBox_2)
        self.ID_Empleado.setObjectName(u"ID_Empleado")
        self.ID_Empleado.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_4.addWidget(self.ID_Empleado, 1, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.tab_Empleados.addTab(self.RegistrarEmpleado, "")
        self.BuscarEmpleado = QWidget()
        self.BuscarEmpleado.setObjectName(u"BuscarEmpleado")
        self.gridLayout_12 = QGridLayout(self.BuscarEmpleado)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_21 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_21, 0, 2, 1, 1)

        self.pushButton_Buscar_Empleado = QPushButton(self.BuscarEmpleado)
        self.pushButton_Buscar_Empleado.setObjectName(u"pushButton_Buscar_Empleado")

        self.gridLayout_12.addWidget(self.pushButton_Buscar_Empleado, 2, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_22, 0, 0, 1, 1)

        self.lineEdit_Buscar_Empleado = QLineEdit(self.BuscarEmpleado)
        self.lineEdit_Buscar_Empleado.setObjectName(u"lineEdit_Buscar_Empleado")

        self.gridLayout_12.addWidget(self.lineEdit_Buscar_Empleado, 2, 0, 1, 2)

        self.tabla_Buscar_Empleado = QTableWidget(self.BuscarEmpleado)
        self.tabla_Buscar_Empleado.setObjectName(u"tabla_Buscar_Empleado")

        self.gridLayout_12.addWidget(self.tabla_Buscar_Empleado, 1, 0, 1, 3)

        self.label_5 = QLabel(self.BuscarEmpleado)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 30))
        self.label_5.setMaximumSize(QSize(1500, 200))
        self.label_5.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_5.setLineWidth(-1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.label_5, 0, 1, 1, 1)

        self.tab_Empleados.addTab(self.BuscarEmpleado, "")
        self.ConsultarEmpleado = QWidget()
        self.ConsultarEmpleado.setObjectName(u"ConsultarEmpleado")
        self.gridLayout_14 = QGridLayout(self.ConsultarEmpleado)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_25 = QSpacerItem(144, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_25, 0, 0, 1, 1)

        self.label_28 = QLabel(self.ConsultarEmpleado)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(30, 30))
        self.label_28.setMaximumSize(QSize(1500, 200))
        self.label_28.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_28.setLineWidth(-1)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_28, 0, 1, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(143, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_24, 0, 2, 1, 1)

        self.tabla_Consultar_Empleado = QTableWidget(self.ConsultarEmpleado)
        self.tabla_Consultar_Empleado.setObjectName(u"tabla_Consultar_Empleado")

        self.gridLayout_14.addWidget(self.tabla_Consultar_Empleado, 1, 0, 1, 3)

        self.pushButton_Mostrar_Empleado = QPushButton(self.ConsultarEmpleado)
        self.pushButton_Mostrar_Empleado.setObjectName(u"pushButton_Mostrar_Empleado")

        self.gridLayout_14.addWidget(self.pushButton_Mostrar_Empleado, 2, 1, 1, 1)

        self.tab_Empleados.addTab(self.ConsultarEmpleado, "")
        self.ModificarEmpleado = QWidget()
        self.ModificarEmpleado.setObjectName(u"ModificarEmpleado")
        self.gridLayout_56 = QGridLayout(self.ModificarEmpleado)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.groupBox_19 = QGroupBox(self.ModificarEmpleado)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_55 = QGridLayout(self.groupBox_19)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setVerticalSpacing(10)
        self.ID_Modificar_Empleado = QLabel(self.groupBox_19)
        self.ID_Modificar_Empleado.setObjectName(u"ID_Modificar_Empleado")
        self.ID_Modificar_Empleado.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_55.addWidget(self.ID_Modificar_Empleado, 3, 4, 1, 1)

        self.label_95 = QLabel(self.groupBox_19)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_55.addWidget(self.label_95, 5, 1, 1, 2)

        self.label_99 = QLabel(self.groupBox_19)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_55.addWidget(self.label_99, 7, 1, 1, 2)

        self.lineEdit_Telefono_Empleado_2 = QLineEdit(self.groupBox_19)
        self.lineEdit_Telefono_Empleado_2.setObjectName(u"lineEdit_Telefono_Empleado_2")

        self.gridLayout_55.addWidget(self.lineEdit_Telefono_Empleado_2, 7, 4, 1, 1)

        self.horizontalSpacer_95 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_95, 5, 0, 1, 1)

        self.verticalSpacer_45 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_55.addItem(self.verticalSpacer_45, 9, 4, 1, 1)

        self.horizontalSpacer_96 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_96, 0, 5, 1, 1)

        self.label_96 = QLabel(self.groupBox_19)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_55.addWidget(self.label_96, 3, 1, 1, 1)

        self.label_100 = QLabel(self.groupBox_19)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_55.addWidget(self.label_100, 4, 1, 1, 2)

        self.comboBox_Cargo_Empleado_2 = QComboBox(self.groupBox_19)
        self.comboBox_Cargo_Empleado_2.addItem("")
        self.comboBox_Cargo_Empleado_2.addItem("")
        self.comboBox_Cargo_Empleado_2.addItem("")
        self.comboBox_Cargo_Empleado_2.addItem("")
        self.comboBox_Cargo_Empleado_2.setObjectName(u"comboBox_Cargo_Empleado_2")

        self.gridLayout_55.addWidget(self.comboBox_Cargo_Empleado_2, 5, 4, 1, 1)

        self.pushButton_Modificar_Empleado = QPushButton(self.groupBox_19)
        self.pushButton_Modificar_Empleado.setObjectName(u"pushButton_Modificar_Empleado")

        self.gridLayout_55.addWidget(self.pushButton_Modificar_Empleado, 8, 4, 1, 1)

        self.comboBox_Estatus_Empleado_2 = QComboBox(self.groupBox_19)
        self.comboBox_Estatus_Empleado_2.addItem("")
        self.comboBox_Estatus_Empleado_2.addItem("")
        self.comboBox_Estatus_Empleado_2.setObjectName(u"comboBox_Estatus_Empleado_2")

        self.gridLayout_55.addWidget(self.comboBox_Estatus_Empleado_2, 6, 4, 1, 1)

        self.label_97 = QLabel(self.groupBox_19)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(30, 30))
        self.label_97.setMaximumSize(QSize(1500, 200))
        self.label_97.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_97.setLineWidth(-1)
        self.label_97.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_97, 0, 4, 1, 1)

        self.label_98 = QLabel(self.groupBox_19)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_55.addWidget(self.label_98, 6, 1, 1, 1)

        self.lineEdit_Nombre_Empleado_2 = QLineEdit(self.groupBox_19)
        self.lineEdit_Nombre_Empleado_2.setObjectName(u"lineEdit_Nombre_Empleado_2")

        self.gridLayout_55.addWidget(self.lineEdit_Nombre_Empleado_2, 4, 4, 1, 1)

        self.verticalSpacer_46 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_55.addItem(self.verticalSpacer_46, 1, 4, 1, 1)

        self.lineEdit_Buscar_Empleado_m = QLineEdit(self.groupBox_19)
        self.lineEdit_Buscar_Empleado_m.setObjectName(u"lineEdit_Buscar_Empleado_m")

        self.gridLayout_55.addWidget(self.lineEdit_Buscar_Empleado_m, 2, 4, 1, 1)

        self.pushButton_Buscar_Empleado_m = QPushButton(self.groupBox_19)
        self.pushButton_Buscar_Empleado_m.setObjectName(u"pushButton_Buscar_Empleado_m")

        self.gridLayout_55.addWidget(self.pushButton_Buscar_Empleado_m, 2, 1, 1, 1)


        self.gridLayout_56.addWidget(self.groupBox_19, 0, 0, 1, 1)

        self.tab_Empleados.addTab(self.ModificarEmpleado, "")

        self.verticalLayout_4.addWidget(self.tab_Empleados)

        self.stackedWidget.addWidget(self.Empleados)
        self.Proveedores = QWidget()
        self.Proveedores.setObjectName(u"Proveedores")
        self.verticalLayout_5 = QVBoxLayout(self.Proveedores)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tab_Proveedores = QTabWidget(self.Proveedores)
        self.tab_Proveedores.setObjectName(u"tab_Proveedores")
        self.tab_Proveedores.setMinimumSize(QSize(30, 30))
        self.tab_Proveedores.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.RegistrarProveedor = QWidget()
        self.RegistrarProveedor.setObjectName(u"RegistrarProveedor")
        self.RegistrarProveedor.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.RegistrarProveedor)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_3 = QGroupBox(self.RegistrarProveedor)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(10)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 7, 4, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_6.addWidget(self.label_22, 4, 1, 1, 2)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_15, 0, 5, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 5, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(30, 30))
        self.label_24.setMaximumSize(QSize(1500, 200))
        self.label_24.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_24.setLineWidth(-1)
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_24, 0, 4, 1, 1)

        self.pushButton_Registrar_Proveedor = QPushButton(self.groupBox_3)
        self.pushButton_Registrar_Proveedor.setObjectName(u"pushButton_Registrar_Proveedor")

        self.gridLayout_6.addWidget(self.pushButton_Registrar_Proveedor, 6, 4, 1, 1)

        self.comboBox_Estatus_Proveedor = QComboBox(self.groupBox_3)
        self.comboBox_Estatus_Proveedor.addItem("")
        self.comboBox_Estatus_Proveedor.addItem("")
        self.comboBox_Estatus_Proveedor.setObjectName(u"comboBox_Estatus_Proveedor")

        self.gridLayout_6.addWidget(self.comboBox_Estatus_Proveedor, 5, 4, 1, 1)

        self.ID_Proveedor = QLabel(self.groupBox_3)
        self.ID_Proveedor.setObjectName(u"ID_Proveedor")
        self.ID_Proveedor.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_6.addWidget(self.ID_Proveedor, 2, 4, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_10, 1, 4, 1, 1)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_6.addWidget(self.label_23, 2, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_13, 4, 0, 1, 1)

        self.lineEdit_Nombre_Proveedor = QLineEdit(self.groupBox_3)
        self.lineEdit_Nombre_Proveedor.setObjectName(u"lineEdit_Nombre_Proveedor")

        self.gridLayout_6.addWidget(self.lineEdit_Nombre_Proveedor, 3, 4, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_6.addWidget(self.label_27, 3, 1, 1, 2)

        self.lineEdit_Telefono_Proveedor = QLineEdit(self.groupBox_3)
        self.lineEdit_Telefono_Proveedor.setObjectName(u"lineEdit_Telefono_Proveedor")

        self.gridLayout_6.addWidget(self.lineEdit_Telefono_Proveedor, 4, 4, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.tab_Proveedores.addTab(self.RegistrarProveedor, "")
        self.BuscarProveedor = QWidget()
        self.BuscarProveedor.setObjectName(u"BuscarProveedor")
        self.gridLayout_13 = QGridLayout(self.BuscarProveedor)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_26 = QLabel(self.BuscarProveedor)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(30, 30))
        self.label_26.setMaximumSize(QSize(1500, 200))
        self.label_26.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_26.setLineWidth(-1)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_26, 0, 1, 1, 2)

        self.tabla_Buscar_Proveedor = QTableWidget(self.BuscarProveedor)
        self.tabla_Buscar_Proveedor.setObjectName(u"tabla_Buscar_Proveedor")

        self.gridLayout_13.addWidget(self.tabla_Buscar_Proveedor, 1, 0, 1, 4)

        self.horizontalSpacer_23 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_23, 0, 3, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(23, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_28, 0, 0, 1, 1)

        self.pushButton_Buscar_Proveedor = QPushButton(self.BuscarProveedor)
        self.pushButton_Buscar_Proveedor.setObjectName(u"pushButton_Buscar_Proveedor")

        self.gridLayout_13.addWidget(self.pushButton_Buscar_Proveedor, 2, 3, 1, 1)

        self.lineEdit_Buscar_Proveedor = QLineEdit(self.BuscarProveedor)
        self.lineEdit_Buscar_Proveedor.setObjectName(u"lineEdit_Buscar_Proveedor")

        self.gridLayout_13.addWidget(self.lineEdit_Buscar_Proveedor, 2, 0, 1, 3)

        self.tab_Proveedores.addTab(self.BuscarProveedor, "")
        self.ConsultarProveedor = QWidget()
        self.ConsultarProveedor.setObjectName(u"ConsultarProveedor")
        self.gridLayout_15 = QGridLayout(self.ConsultarProveedor)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_27 = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_27, 0, 0, 1, 1)

        self.label_29 = QLabel(self.ConsultarProveedor)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(30, 30))
        self.label_29.setMaximumSize(QSize(1500, 200))
        self.label_29.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_29.setLineWidth(-1)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_29, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_26, 0, 2, 1, 1)

        self.tabla_Consultar_Proveedor = QTableWidget(self.ConsultarProveedor)
        self.tabla_Consultar_Proveedor.setObjectName(u"tabla_Consultar_Proveedor")

        self.gridLayout_15.addWidget(self.tabla_Consultar_Proveedor, 1, 0, 1, 3)

        self.pushButton_Mostrar_Proveedor = QPushButton(self.ConsultarProveedor)
        self.pushButton_Mostrar_Proveedor.setObjectName(u"pushButton_Mostrar_Proveedor")

        self.gridLayout_15.addWidget(self.pushButton_Mostrar_Proveedor, 2, 1, 1, 1)

        self.tab_Proveedores.addTab(self.ConsultarProveedor, "")
        self.ModificarProveedor = QWidget()
        self.ModificarProveedor.setObjectName(u"ModificarProveedor")
        self.gridLayout_58 = QGridLayout(self.ModificarProveedor)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.groupBox_20 = QGroupBox(self.ModificarProveedor)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.gridLayout_57 = QGridLayout(self.groupBox_20)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setVerticalSpacing(10)
        self.comboBox_Estatus_Proveedor_2 = QComboBox(self.groupBox_20)
        self.comboBox_Estatus_Proveedor_2.addItem("")
        self.comboBox_Estatus_Proveedor_2.addItem("")
        self.comboBox_Estatus_Proveedor_2.setObjectName(u"comboBox_Estatus_Proveedor_2")

        self.gridLayout_57.addWidget(self.comboBox_Estatus_Proveedor_2, 6, 4, 1, 1)

        self.ID_Modficar_Proveedor = QLabel(self.groupBox_20)
        self.ID_Modficar_Proveedor.setObjectName(u"ID_Modficar_Proveedor")
        self.ID_Modficar_Proveedor.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_57.addWidget(self.ID_Modficar_Proveedor, 3, 4, 1, 1)

        self.horizontalSpacer_98 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_98, 5, 0, 1, 1)

        self.label_104 = QLabel(self.groupBox_20)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_57.addWidget(self.label_104, 3, 1, 1, 1)

        self.verticalSpacer_48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_57.addItem(self.verticalSpacer_48, 1, 4, 1, 1)

        self.label_103 = QLabel(self.groupBox_20)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(30, 30))
        self.label_103.setMaximumSize(QSize(1500, 200))
        self.label_103.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_103.setLineWidth(-1)
        self.label_103.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_57.addWidget(self.label_103, 0, 4, 1, 1)

        self.pushButton_Modificar_Proveedor = QPushButton(self.groupBox_20)
        self.pushButton_Modificar_Proveedor.setObjectName(u"pushButton_Modificar_Proveedor")

        self.gridLayout_57.addWidget(self.pushButton_Modificar_Proveedor, 7, 4, 1, 1)

        self.lineEdit_Telefono_Proveedor_2 = QLineEdit(self.groupBox_20)
        self.lineEdit_Telefono_Proveedor_2.setObjectName(u"lineEdit_Telefono_Proveedor_2")

        self.gridLayout_57.addWidget(self.lineEdit_Telefono_Proveedor_2, 5, 4, 1, 1)

        self.label_105 = QLabel(self.groupBox_20)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_57.addWidget(self.label_105, 4, 1, 1, 2)

        self.label_101 = QLabel(self.groupBox_20)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_57.addWidget(self.label_101, 5, 1, 1, 2)

        self.lineEdit_Nombre_Proveedor_2 = QLineEdit(self.groupBox_20)
        self.lineEdit_Nombre_Proveedor_2.setObjectName(u"lineEdit_Nombre_Proveedor_2")

        self.gridLayout_57.addWidget(self.lineEdit_Nombre_Proveedor_2, 4, 4, 1, 1)

        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_57.addItem(self.horizontalSpacer_97, 0, 5, 1, 1)

        self.label_102 = QLabel(self.groupBox_20)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_57.addWidget(self.label_102, 6, 1, 1, 1)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_57.addItem(self.verticalSpacer_47, 8, 4, 1, 1)

        self.pushButton_Buscar_Proveedor_m = QPushButton(self.groupBox_20)
        self.pushButton_Buscar_Proveedor_m.setObjectName(u"pushButton_Buscar_Proveedor_m")

        self.gridLayout_57.addWidget(self.pushButton_Buscar_Proveedor_m, 2, 1, 1, 1)

        self.lineEdit_Buscar_Proveedor_m = QLineEdit(self.groupBox_20)
        self.lineEdit_Buscar_Proveedor_m.setObjectName(u"lineEdit_Buscar_Proveedor_m")

        self.gridLayout_57.addWidget(self.lineEdit_Buscar_Proveedor_m, 2, 4, 1, 1)


        self.gridLayout_58.addWidget(self.groupBox_20, 0, 0, 1, 1)

        self.tab_Proveedores.addTab(self.ModificarProveedor, "")

        self.verticalLayout_5.addWidget(self.tab_Proveedores)

        self.stackedWidget.addWidget(self.Proveedores)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Paginas)


        self.gridLayout_3.addWidget(self.FrameInf, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tab_Comandas.setCurrentIndex(3)
        self.tab_Platillos.setCurrentIndex(3)
        self.tab_Compras.setCurrentIndex(0)
        self.tab_Insumo.setCurrentIndex(2)
        self.tab_Empleados.setCurrentIndex(3)
        self.tab_Proveedores.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonHamburguesa.setText("")
        self.pushButtonComandas.setText(QCoreApplication.translate("MainWindow", u"Comandas", None))
        self.pushButtonPlatillos.setText(QCoreApplication.translate("MainWindow", u"Platillos", None))
        self.pushButtonCompras.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.pushButtonInsumos.setText(QCoreApplication.translate("MainWindow", u"Insumos", None))
        self.pushButtonEmpleados.setText(QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.pushButtonProveedores.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.Fondo.setText("")
        self.comboBox_Estatus_Comanda.setItemText(0, QCoreApplication.translate("MainWindow", u"Pendiente", None))
        self.comboBox_Estatus_Comanda.setItemText(1, QCoreApplication.translate("MainWindow", u"Pagada", None))

        self.label_ID_4.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.ID_Comanda.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.groupBox_6.setTitle("")
        self.Label_Descripcion_Platillo_Comanda.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_Agregar_Platillos_Comanda.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pushButton_Registrar_Comanda.setText(QCoreApplication.translate("MainWindow", u"Registrar comanda", None))
        self.Label_Precio_Platillo_Comanda.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_Buscar_Platillos_Comanda.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_ID_Platillo.setText("")
        self.lineEdit_ID_Platillo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del platillo", None))
        self.label_ID_14.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Platillos:", None))
        self.Label_Nombre_Platillo_Comanda.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_ID_12.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_ID_13.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.groupBox_5.setTitle("")
        self.label_ID_5.setText(QCoreApplication.translate("MainWindow", u"Subtotal:", None))
        self.Subtotal.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Total.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.IVA.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_ID_11.setText(QCoreApplication.translate("MainWindow", u"TOTAL:", None))
        self.label_ID_10.setText(QCoreApplication.translate("MainWindow", u"IVA:", None))
        self.fecha_comanda.setText(QCoreApplication.translate("MainWindow", u"dd/mm/aaaa", None))
        self.label_Titulo_Registrar_3.setText(QCoreApplication.translate("MainWindow", u"Registrar Nueva Comanda", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.RegistrarComanda), QCoreApplication.translate("MainWindow", u"Registrar comanda", None))
        self.label_Titulo_Registrar_5.setText(QCoreApplication.translate("MainWindow", u"Buscar Comanda", None))
        self.Label_Estatus_Comanda_Buscar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_ID_19.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.groupBox_7.setTitle("")
        self.label_ID_15.setText(QCoreApplication.translate("MainWindow", u"Subtotal:", None))
        self.Subtotal_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Total_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.IVA_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_ID_16.setText(QCoreApplication.translate("MainWindow", u"TOTAL:", None))
        self.label_ID_17.setText(QCoreApplication.translate("MainWindow", u"IVA:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"PLATILLOS", None))
        self.pushButton_Buscar_Comanda.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.lineEdit_ID_Buscar_Comanda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el ID de la comanda", None))
        self.fecha_buscar_comadna.setText(QCoreApplication.translate("MainWindow", u"dd/mm/aaaa", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.BuscarComanda), QCoreApplication.translate("MainWindow", u"Buscar comanda", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.ConsultarComanda), QCoreApplication.translate("MainWindow", u"Listado comandas", None))
        self.label_Titulo_Registrar_6.setText(QCoreApplication.translate("MainWindow", u"Modificar Comanda", None))
        self.label_ID_20.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.pushButton_Modificar_Comanda.setText(QCoreApplication.translate("MainWindow", u"Guardar cambios", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.groupBox_9.setTitle("")
        self.label_ID_18.setText(QCoreApplication.translate("MainWindow", u"Subtotal:", None))
        self.Subtotal_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Total_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.IVA_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_ID_21.setText(QCoreApplication.translate("MainWindow", u"TOTAL:", None))
        self.label_ID_22.setText(QCoreApplication.translate("MainWindow", u"IVA:", None))
        self.lineEdit_ID_Comand_Modificar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el ID de la comanda", None))
        self.comboBox_Estatus_Comanda_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Pendiente", None))
        self.comboBox_Estatus_Comanda_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Pagada", None))

        self.pushButton_Buscar_Comanda_Modificar.setText(QCoreApplication.translate("MainWindow", u"BUSCAR", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"dd/mm/aaaa", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"PLATILLOS", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.ModificarComanda), QCoreApplication.translate("MainWindow", u"Modificar comanda", None))
        self.comboBox_Estatus_Platillo.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Platillo.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_Existencia_3.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.label_Titulo_Registrar_2.setText(QCoreApplication.translate("MainWindow", u"Registrar Nuevo Platillo", None))
        self.ID_Platillo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.label_ID_3.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_Descripcion_3.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.groupBox.setTitle("")
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Insumos:", None))
        self.lineEdit_ID_Insumos_Platillo.setText("")
        self.lineEdit_ID_Insumos_Platillo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el ID del insumo a buscar", None))
        self.pushButton_Buscar_Insumos_ID.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_ID_7.setText(QCoreApplication.translate("MainWindow", u"Nombre Inusmo:", None))
        self.Label_Nombre_Insumo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_Agregar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_ID_8.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.Label_Descripcion_Insumo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_ID_9.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_Nombre_Insumo_3.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.pushButton_Registrar_Platillo.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo Platillo", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.RegistrarPlatillo), QCoreApplication.translate("MainWindow", u"Registrar platillo", None))
        self.label_Titulo_Registrar_7.setText(QCoreApplication.translate("MainWindow", u"Buscar Platillo", None))
        self.label_ID_26.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_Nombre_Insumo_5.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.Nombre_Platillo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_Existencia_4.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.Precio_Platillo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_Descripcion_4.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.Descripcion_Platillo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.Esatus_Platillo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"INSUMOS", None))
        self.pushButton_Buscar_Platillo.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_ID_Buscar_Platillo.setText("")
        self.lineEdit_ID_Buscar_Platillo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el ID del platillo a buscar", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.BuscarPlatillo), QCoreApplication.translate("MainWindow", u"Buscar platillo", None))
        self.Titulo_Consultar_Insumo_2.setText(QCoreApplication.translate("MainWindow", u"Listado de Platillos", None))
        self.pushButton_Mostrar_Platillos.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.ConsultarPlatillo), QCoreApplication.translate("MainWindow", u"Listado platillo", None))
        self.groupBox_12.setTitle("")
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Insumos:", None))
        self.lineEdit_ID_Insumos_Platillo_Modificar.setText("")
        self.lineEdit_ID_Insumos_Platillo_Modificar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el ID del insumo a buscar", None))
        self.pushButton_Buscar_Insumos_Modificar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_ID_23.setText(QCoreApplication.translate("MainWindow", u"Nombre Inusmo:", None))
        self.Label_Nombre_Insumo_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_Agregar_Insumo_2.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_ID_24.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.Label_Descripcion_Insumo_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_ID_25.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.pushButton_Quitar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Quitar", None))
        self.label_Nombre_Insumo_6.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_Existencia_5.setText(QCoreApplication.translate("MainWindow", u"Precio:", None))
        self.comboBox_Estatus_Platillo_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Platillo_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_Titulo_Registrar_8.setText(QCoreApplication.translate("MainWindow", u"Modificar Platillo", None))
        self.label_ID_27.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Estatus:", None))
        self.pushButton_Modificar_Platillo.setText(QCoreApplication.translate("MainWindow", u"Guardar Cambios", None))
        self.label_Descripcion_5.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.lineEdit_ID_Platillo_Modificar.setText("")
        self.lineEdit_ID_Platillo_Modificar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el ID del platillo a buscar", None))
        self.pushButton_Buscar_Platillo_Modificar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.ModificarPlatillo), QCoreApplication.translate("MainWindow", u"Modificar platillo", None))
        self.label_Titulo_Registrar_4.setText(QCoreApplication.translate("MainWindow", u"Registrar Nueva Compra", None))
        self.fecha_compra.setText(QCoreApplication.translate("MainWindow", u"dd/mm/aaaa", None))
        self.label_ID_6.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.ID_Compra.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_Nombre_Insumo_4.setText(QCoreApplication.translate("MainWindow", u"Proveedor:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Insumos:", None))
        self.lineEdit_ID_Insumos_Compra.setText("")
        self.lineEdit_ID_Insumos_Compra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del insumo", None))
        self.pushButton_Buscar_Insumos_Compra.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_Registrar_Compra.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo Compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.RegistrarCompra), QCoreApplication.translate("MainWindow", u"Registrar compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.BuscarCompra), QCoreApplication.translate("MainWindow", u"Buscar compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.ConsultarCompra), QCoreApplication.translate("MainWindow", u"Listado compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.ModificarCompra), QCoreApplication.translate("MainWindow", u"Modificar compra", None))
        self.groupBoxInsumo.setTitle("")
        self.pushButton_Registrar_Inusmo.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo insumo", None))
        self.label_Descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_Existencia.setText(QCoreApplication.translate("MainWindow", u"Existencias:", None))
        self.ID_Insumo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_Nombre_Insumo.setText(QCoreApplication.translate("MainWindow", u"Nombre del insumo:", None))
        self.label_Titulo_Registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar Nuevo Insumo", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.RegistrarInsumo), QCoreApplication.translate("MainWindow", u"Registrar insumo", None))
        self.pushButton_Buscar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_Titutlo_Busqueda.setText(QCoreApplication.translate("MainWindow", u"Busqueda de insumo por ID", None))
        self.lineEdit_Buscar_Insumo.setText("")
        self.lineEdit_Buscar_Insumo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del insumo", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.BuscarInsumo), QCoreApplication.translate("MainWindow", u"Buscar insumo", None))
        self.Titulo_Consultar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Listado de Insumos", None))
        self.pushButton_Mostrar_Insumos.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.ConsultarInsumo), QCoreApplication.translate("MainWindow", u"Listado insumo", None))
        self.groupBox_4.setTitle("")
        self.label_Nombre_Insumo_2.setText(QCoreApplication.translate("MainWindow", u"Nombre del insumo:", None))
        self.label_ID_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.pushButton_Buscar_Insum_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Insumo_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del insumo", None))
        self.ID_Modificar_Insumo.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_Descripcion_2.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.pushButton_Modificar_Inusmo.setText(QCoreApplication.translate("MainWindow", u"Guardar cambios", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Modificar Insumo", None))
        self.label_Existencia_2.setText(QCoreApplication.translate("MainWindow", u"Existencias:", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.ModificarInsumo), QCoreApplication.translate("MainWindow", u"Modificar insumo", None))
        self.groupBox_2.setTitle("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.comboBox_Cargo_Empleado.setItemText(0, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.comboBox_Cargo_Empleado.setItemText(1, QCoreApplication.translate("MainWindow", u"Cajero", None))
        self.comboBox_Cargo_Empleado.setItemText(2, QCoreApplication.translate("MainWindow", u"Repartidor", None))
        self.comboBox_Cargo_Empleado.setItemText(3, QCoreApplication.translate("MainWindow", u"Cocinero", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Registrar Nuevo Empleado", None))
        self.pushButton_Registrar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo Empleado", None))
        self.comboBox_Estatus_Empleado.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Empleado.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.ID_Empleado.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.RegistrarEmpleado), QCoreApplication.translate("MainWindow", u"Registrar empleado", None))
        self.pushButton_Buscar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Empleado.setText("")
        self.lineEdit_Buscar_Empleado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Empleado", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Busqueda de Empleado por ID", None))
        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.BuscarEmpleado), QCoreApplication.translate("MainWindow", u"Buscar empleado", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Listado de Empleados", None))
        self.pushButton_Mostrar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.ConsultarEmpleado), QCoreApplication.translate("MainWindow", u"Listado empleado", None))
        self.groupBox_19.setTitle("")
        self.ID_Modificar_Empleado.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.comboBox_Cargo_Empleado_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.comboBox_Cargo_Empleado_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cocinero", None))
        self.comboBox_Cargo_Empleado_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cajero", None))
        self.comboBox_Cargo_Empleado_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Repartidor", None))

        self.pushButton_Modificar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Guardar cambios", None))
        self.comboBox_Estatus_Empleado_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Empleado_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Modificar Empleado", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.lineEdit_Buscar_Empleado_m.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Empleado", None))
        self.pushButton_Buscar_Empleado_m.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.ModificarEmpleado), QCoreApplication.translate("MainWindow", u"Modificar empleado", None))
        self.groupBox_3.setTitle("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Registrar Nuevo Proveedor", None))
        self.pushButton_Registrar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo Proveedor", None))
        self.comboBox_Estatus_Proveedor.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Proveedor.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.ID_Proveedor.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.tab_Proveedores.setTabText(self.tab_Proveedores.indexOf(self.RegistrarProveedor), QCoreApplication.translate("MainWindow", u"Registrar proveedor", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Busqueda de Proveedor por ID", None))
        self.pushButton_Buscar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Proveedor.setText("")
        self.lineEdit_Buscar_Proveedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Proveedor", None))
        self.tab_Proveedores.setTabText(self.tab_Proveedores.indexOf(self.BuscarProveedor), QCoreApplication.translate("MainWindow", u"Buscar proveedor", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Listado de Proveedores", None))
        self.pushButton_Mostrar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tab_Proveedores.setTabText(self.tab_Proveedores.indexOf(self.ConsultarProveedor), QCoreApplication.translate("MainWindow", u"Listado proveedor", None))
        self.groupBox_20.setTitle("")
        self.comboBox_Estatus_Proveedor_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Proveedor_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.ID_Modficar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Modificar Proveedor", None))
        self.pushButton_Modificar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Guardar cambios", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.pushButton_Buscar_Proveedor_m.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Proveedor_m.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Proveedor", None))
        self.tab_Proveedores.setTabText(self.tab_Proveedores.indexOf(self.ModificarProveedor), QCoreApplication.translate("MainWindow", u"Modificar proveedor", None))
    # retranslateUi

