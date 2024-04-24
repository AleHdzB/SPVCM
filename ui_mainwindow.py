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
        MainWindow.resize(813, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.pushButtonHamburguesa.setIconSize(QSize(32, 32))

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


        self.verticalLayout_2.addWidget(self.FrameSup)

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
        self.tab_Comandas.addTab(self.RegistrarComanda, "")
        self.BuscarComanda = QWidget()
        self.BuscarComanda.setObjectName(u"BuscarComanda")
        self.tab_Comandas.addTab(self.BuscarComanda, "")
        self.ConsultarComanda = QWidget()
        self.ConsultarComanda.setObjectName(u"ConsultarComanda")
        self.tab_Comandas.addTab(self.ConsultarComanda, "")
        self.ModificarComanda = QWidget()
        self.ModificarComanda.setObjectName(u"ModificarComanda")
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
        self.tab_Platillos.addTab(self.RegistrarPlatillo, "")
        self.BuscarPlatillo = QWidget()
        self.BuscarPlatillo.setObjectName(u"BuscarPlatillo")
        self.tab_Platillos.addTab(self.BuscarPlatillo, "")
        self.ConsultarPlatillo = QWidget()
        self.ConsultarPlatillo.setObjectName(u"ConsultarPlatillo")
        self.tab_Platillos.addTab(self.ConsultarPlatillo, "")
        self.ModificarPlatillo = QWidget()
        self.ModificarPlatillo.setObjectName(u"ModificarPlatillo")
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
        self.tab_Compras.addTab(self.RegistrarCompra, "")
        self.BuscarCompra = QWidget()
        self.BuscarCompra.setObjectName(u"BuscarCompra")
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

        self.pushButton_Limiar_Insumo = QPushButton(self.ConsultarInsumo)
        self.pushButton_Limiar_Insumo.setObjectName(u"pushButton_Limiar_Insumo")

        self.gridLayout_9.addWidget(self.pushButton_Limiar_Insumo, 2, 2, 1, 1)

        self.pushButton_Mostrar_Insumos = QPushButton(self.ConsultarInsumo)
        self.pushButton_Mostrar_Insumos.setObjectName(u"pushButton_Mostrar_Insumos")

        self.gridLayout_9.addWidget(self.pushButton_Mostrar_Insumos, 2, 0, 1, 1)

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
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(1500, 200))
        self.label_2.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_2.setLineWidth(-1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_2, 0, 3, 1, 1)

        self.pushButton_Modificar_Inusmo = QPushButton(self.groupBox_4)
        self.pushButton_Modificar_Inusmo.setObjectName(u"pushButton_Modificar_Inusmo")

        self.gridLayout_10.addWidget(self.pushButton_Modificar_Inusmo, 7, 3, 1, 1)

        self.lineEdit_Buscar_Insumo_5 = QLineEdit(self.groupBox_4)
        self.lineEdit_Buscar_Insumo_5.setObjectName(u"lineEdit_Buscar_Insumo_5")

        self.gridLayout_10.addWidget(self.lineEdit_Buscar_Insumo_5, 1, 2, 1, 2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_20, 0, 4, 1, 1)

        self.label_Existencia_2 = QLabel(self.groupBox_4)
        self.label_Existencia_2.setObjectName(u"label_Existencia_2")
        self.label_Existencia_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_10.addWidget(self.label_Existencia_2, 5, 1, 1, 2)

        self.lineEdit_Nombre_Insumo_2 = QLineEdit(self.groupBox_4)
        self.lineEdit_Nombre_Insumo_2.setObjectName(u"lineEdit_Nombre_Insumo_2")

        self.gridLayout_10.addWidget(self.lineEdit_Nombre_Insumo_2, 4, 3, 1, 1)

        self.label_Nombre_Insumo_2 = QLabel(self.groupBox_4)
        self.label_Nombre_Insumo_2.setObjectName(u"label_Nombre_Insumo_2")
        self.label_Nombre_Insumo_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_10.addWidget(self.label_Nombre_Insumo_2, 4, 1, 1, 2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_19, 5, 0, 1, 1)

        self.ID_Modificar_Insumo = QLabel(self.groupBox_4)
        self.ID_Modificar_Insumo.setObjectName(u"ID_Modificar_Insumo")
        self.ID_Modificar_Insumo.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_10.addWidget(self.ID_Modificar_Insumo, 3, 3, 1, 1)

        self.SpinBox_Existencia_2 = QDoubleSpinBox(self.groupBox_4)
        self.SpinBox_Existencia_2.setObjectName(u"SpinBox_Existencia_2")

        self.gridLayout_10.addWidget(self.SpinBox_Existencia_2, 5, 3, 1, 1)

        self.textEdit_Descripcion_2 = QTextEdit(self.groupBox_4)
        self.textEdit_Descripcion_2.setObjectName(u"textEdit_Descripcion_2")

        self.gridLayout_10.addWidget(self.textEdit_Descripcion_2, 6, 3, 1, 1)

        self.label_ID_2 = QLabel(self.groupBox_4)
        self.label_ID_2.setObjectName(u"label_ID_2")
        self.label_ID_2.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_10.addWidget(self.label_ID_2, 3, 1, 1, 1)

        self.label_Descripcion_2 = QLabel(self.groupBox_4)
        self.label_Descripcion_2.setObjectName(u"label_Descripcion_2")
        self.label_Descripcion_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_10.addWidget(self.label_Descripcion_2, 6, 1, 1, 2)

        self.pushButton_Buscar_Insum_2 = QPushButton(self.groupBox_4)
        self.pushButton_Buscar_Insum_2.setObjectName(u"pushButton_Buscar_Insum_2")

        self.gridLayout_10.addWidget(self.pushButton_Buscar_Insum_2, 1, 1, 1, 1)


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
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(10)
        self.pushButton_Registrar_Empleado = QPushButton(self.groupBox_2)
        self.pushButton_Registrar_Empleado.setObjectName(u"pushButton_Registrar_Empleado")

        self.gridLayout_5.addWidget(self.pushButton_Registrar_Empleado, 7, 4, 1, 1)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_5.addWidget(self.label_18, 4, 1, 1, 2)

        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);\n"
"")

        self.gridLayout_5.addWidget(self.label_17, 2, 1, 1, 1)

        self.comboBox_Estatus_Empleado = QComboBox(self.groupBox_2)
        self.comboBox_Estatus_Empleado.addItem("")
        self.comboBox_Estatus_Empleado.addItem("")
        self.comboBox_Estatus_Empleado.setObjectName(u"comboBox_Estatus_Empleado")

        self.gridLayout_5.addWidget(self.comboBox_Estatus_Empleado, 5, 4, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 8, 4, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 30))
        self.label_20.setMaximumSize(QSize(1500, 200))
        self.label_20.setStyleSheet(u"font: 75 36pt \"MS Shell Dlg 2\";")
        self.label_20.setLineWidth(-1)
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_20, 0, 4, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 4, 0, 1, 1)

        self.ID_Empleado = QLabel(self.groupBox_2)
        self.ID_Empleado.setObjectName(u"ID_Empleado")
        self.ID_Empleado.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_5.addWidget(self.ID_Empleado, 2, 4, 1, 1)

        self.label_21 = QLabel(self.groupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_5.addWidget(self.label_21, 5, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_14, 0, 5, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_5.addWidget(self.label_16, 6, 1, 1, 2)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_5.addWidget(self.label_19, 3, 1, 1, 2)

        self.lineEdit_Telefono_Empleado = QLineEdit(self.groupBox_2)
        self.lineEdit_Telefono_Empleado.setObjectName(u"lineEdit_Telefono_Empleado")

        self.gridLayout_5.addWidget(self.lineEdit_Telefono_Empleado, 6, 4, 1, 1)

        self.comboBox_Cargo_Empleado = QComboBox(self.groupBox_2)
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.addItem("")
        self.comboBox_Cargo_Empleado.setObjectName(u"comboBox_Cargo_Empleado")

        self.gridLayout_5.addWidget(self.comboBox_Cargo_Empleado, 4, 4, 1, 1)

        self.lineEdit_Nombre_Empleado = QLineEdit(self.groupBox_2)
        self.lineEdit_Nombre_Empleado.setObjectName(u"lineEdit_Nombre_Empleado")

        self.gridLayout_5.addWidget(self.lineEdit_Nombre_Empleado, 3, 4, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 1, 4, 1, 1)


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

        self.gridLayout_14.addWidget(self.pushButton_Mostrar_Empleado, 2, 0, 1, 1)

        self.pushButton_Limiar_Empleado = QPushButton(self.ConsultarEmpleado)
        self.pushButton_Limiar_Empleado.setObjectName(u"pushButton_Limiar_Empleado")

        self.gridLayout_14.addWidget(self.pushButton_Limiar_Empleado, 2, 2, 1, 1)

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
        self.proveedor = QTabWidget(self.Proveedores)
        self.proveedor.setObjectName(u"proveedor")
        self.proveedor.setMinimumSize(QSize(30, 30))
        self.proveedor.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
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

        self.proveedor.addTab(self.RegistrarProveedor, "")
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

        self.proveedor.addTab(self.BuscarProveedor, "")
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

        self.gridLayout_15.addWidget(self.pushButton_Mostrar_Proveedor, 2, 0, 1, 1)

        self.pushButton_Limiar_Proveedor = QPushButton(self.ConsultarProveedor)
        self.pushButton_Limiar_Proveedor.setObjectName(u"pushButton_Limiar_Proveedor")

        self.gridLayout_15.addWidget(self.pushButton_Limiar_Proveedor, 2, 2, 1, 1)

        self.proveedor.addTab(self.ConsultarProveedor, "")
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

        self.ID_Modificar_Insumo_m = QLabel(self.groupBox_20)
        self.ID_Modificar_Insumo_m.setObjectName(u"ID_Modificar_Insumo_m")
        self.ID_Modificar_Insumo_m.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 170, 127);")

        self.gridLayout_57.addWidget(self.ID_Modificar_Insumo_m, 3, 4, 1, 1)

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

        self.proveedor.addTab(self.ModificarProveedor, "")

        self.verticalLayout_5.addWidget(self.proveedor)

        self.stackedWidget.addWidget(self.Proveedores)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Paginas)


        self.verticalLayout_2.addWidget(self.FrameInf)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)
        self.tab_Comandas.setCurrentIndex(2)
        self.tab_Platillos.setCurrentIndex(0)
        self.tab_Compras.setCurrentIndex(1)
        self.tab_Insumo.setCurrentIndex(3)
        self.tab_Empleados.setCurrentIndex(3)
        self.proveedor.setCurrentIndex(3)


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
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.RegistrarComanda), QCoreApplication.translate("MainWindow", u"Registrar comanda", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.BuscarComanda), QCoreApplication.translate("MainWindow", u"Buscar comanda", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.ConsultarComanda), QCoreApplication.translate("MainWindow", u"Listado comandas", None))
        self.tab_Comandas.setTabText(self.tab_Comandas.indexOf(self.ModificarComanda), QCoreApplication.translate("MainWindow", u"Modificar comanda", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.RegistrarPlatillo), QCoreApplication.translate("MainWindow", u"Registrar platillo", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.BuscarPlatillo), QCoreApplication.translate("MainWindow", u"Buscar platillo", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.ConsultarPlatillo), QCoreApplication.translate("MainWindow", u"Listado platillo", None))
        self.tab_Platillos.setTabText(self.tab_Platillos.indexOf(self.ModificarPlatillo), QCoreApplication.translate("MainWindow", u"Modificar platillo", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.RegistrarCompra), QCoreApplication.translate("MainWindow", u"Registrar compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.BuscarCompra), QCoreApplication.translate("MainWindow", u"Buscar compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.ConsultarCompra), QCoreApplication.translate("MainWindow", u"Listado compra", None))
        self.tab_Compras.setTabText(self.tab_Compras.indexOf(self.ModificarCompra), QCoreApplication.translate("MainWindow", u"Modificar compra", None))
        self.groupBoxInsumo.setTitle("")
        self.pushButton_Registrar_Inusmo.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo insumo", None))
        self.label_Descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_ID.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_Existencia.setText(QCoreApplication.translate("MainWindow", u"Existencias:", None))
        self.ID_Insumo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_Nombre_Insumo.setText(QCoreApplication.translate("MainWindow", u"Nombre del insumo:", None))
        self.label_Titulo_Registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar Nuevo Insumo", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.RegistrarInsumo), QCoreApplication.translate("MainWindow", u"Registrar insumo", None))
        self.pushButton_Buscar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_Titutlo_Busqueda.setText(QCoreApplication.translate("MainWindow", u"Busqueda de insumo por ID", None))
        self.lineEdit_Buscar_Insumo.setText("")
        self.lineEdit_Buscar_Insumo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del insumo", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.BuscarInsumo), QCoreApplication.translate("MainWindow", u"Buscar insumo", None))
        self.Titulo_Consultar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Listado de Insumos", None))
        self.pushButton_Limiar_Insumo.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pushButton_Mostrar_Insumos.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.ConsultarInsumo), QCoreApplication.translate("MainWindow", u"Listado insumo", None))
        self.groupBox_4.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Modificar Insumo", None))
        self.pushButton_Modificar_Inusmo.setText(QCoreApplication.translate("MainWindow", u"Guardar cambios", None))
        self.lineEdit_Buscar_Insumo_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del insumo", None))
        self.label_Existencia_2.setText(QCoreApplication.translate("MainWindow", u"Existencias:", None))
        self.label_Nombre_Insumo_2.setText(QCoreApplication.translate("MainWindow", u"Nombre del insumo:", None))
        self.ID_Modificar_Insumo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_ID_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_Descripcion_2.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.pushButton_Buscar_Insum_2.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tab_Insumo.setTabText(self.tab_Insumo.indexOf(self.ModificarInsumo), QCoreApplication.translate("MainWindow", u"Modificar insumo", None))
        self.groupBox_2.setTitle("")
        self.pushButton_Registrar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo insumo", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.comboBox_Estatus_Empleado.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Empleado.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Registrar Nuevo Empleado", None))
        self.ID_Empleado.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.comboBox_Cargo_Empleado.setItemText(0, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.comboBox_Cargo_Empleado.setItemText(1, QCoreApplication.translate("MainWindow", u"Cajero", None))
        self.comboBox_Cargo_Empleado.setItemText(2, QCoreApplication.translate("MainWindow", u"Repartidor", None))
        self.comboBox_Cargo_Empleado.setItemText(3, QCoreApplication.translate("MainWindow", u"Cocinero", None))

        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.RegistrarEmpleado), QCoreApplication.translate("MainWindow", u"Registrar empleado", None))
        self.pushButton_Buscar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Empleado.setText("")
        self.lineEdit_Buscar_Empleado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Empleado", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Busqueda de Empleado por ID", None))
        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.BuscarEmpleado), QCoreApplication.translate("MainWindow", u"Buscar empleado", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Listado de Empleados", None))
        self.pushButton_Mostrar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_Limiar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tab_Empleados.setTabText(self.tab_Empleados.indexOf(self.ConsultarEmpleado), QCoreApplication.translate("MainWindow", u"Listado empleado", None))
        self.groupBox_19.setTitle("")
        self.ID_Modificar_Empleado.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Cargo:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.comboBox_Cargo_Empleado_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.comboBox_Cargo_Empleado_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cocinero", None))
        self.comboBox_Cargo_Empleado_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cajero", None))
        self.comboBox_Cargo_Empleado_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Repartidor", None))

        self.pushButton_Modificar_Empleado.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo insumo", None))
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
        self.pushButton_Registrar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo insumo", None))
        self.comboBox_Estatus_Proveedor.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Proveedor.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.ID_Proveedor.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.proveedor.setTabText(self.proveedor.indexOf(self.RegistrarProveedor), QCoreApplication.translate("MainWindow", u"Registrar proveedor", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Busqueda de Proveedor por ID", None))
        self.pushButton_Buscar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Proveedor.setText("")
        self.lineEdit_Buscar_Proveedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Proveedor", None))
        self.proveedor.setTabText(self.proveedor.indexOf(self.BuscarProveedor), QCoreApplication.translate("MainWindow", u"Buscar proveedor", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Listado de Proveedores", None))
        self.pushButton_Mostrar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.pushButton_Limiar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.proveedor.setTabText(self.proveedor.indexOf(self.ConsultarProveedor), QCoreApplication.translate("MainWindow", u"Listado proveedor", None))
        self.groupBox_20.setTitle("")
        self.comboBox_Estatus_Proveedor_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Activo", None))
        self.comboBox_Estatus_Proveedor_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Inactivo", None))

        self.ID_Modificar_Insumo_m.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Modificar Proveedor", None))
        self.pushButton_Modificar_Proveedor.setText(QCoreApplication.translate("MainWindow", u"Registrar nuevo insumo", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Telefono:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.pushButton_Buscar_Proveedor_m.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.lineEdit_Buscar_Proveedor_m.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese el Identificador del Proveedor", None))
        self.proveedor.setTabText(self.proveedor.indexOf(self.ModificarProveedor), QCoreApplication.translate("MainWindow", u"Modificar proveedor", None))
    # retranslateUi

