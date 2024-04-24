from PySide2.QtWidgets import QMainWindow,QMessageBox, QTableWidgetItem, QStackedWidget
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import sqlite3
from Metodos import *
from PySide2.QtCore import Qt


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    # Obtén una referencia al QStackedWidget desde el diseño
    self.stackedWidget = self.ui.stackedWidget

    #Navegacion 
    self.ui.pushButtonHamburguesa.clicked.connect(self.navegar_inicio)
    self.ui.pushButtonComandas.clicked.connect(self.navegar_comandas)
    self.ui.pushButtonCompras.clicked.connect(self.navegar_compras)
    self.ui.pushButtonPlatillos.clicked.connect(self.navegar_platillos)
    self.ui.pushButtonInsumos.clicked.connect(self.navegar_insumos)
    self.ui.pushButtonEmpleados.clicked.connect(self.navegar_empleados)
    self.ui.pushButtonProveedores.clicked.connect(self.navegar_provedores)

        # Establecer el índice inicial del QStackedWidget en 0
    self.stackedWidget.setCurrentIndex(0)
    #REGISTRO de datos en la Base de Datos
    self.ui.pushButton_Registrar_Inusmo.clicked.connect(self.registrar_inusmo)
    self.ui.pushButton_Registrar_Empleado.clicked.connect(self.registrar_empleado)
    #BUSQUEDA de datos en la Base de Datos
    self.ui.pushButton_Buscar_Insumo.clicked.connect(self.buscar_insumo)
    #CONSULTAR datos en la Base de Datos
    #MODIFICAR datos en la Base de Datos
    self.ui.pushButton_Buscar_Insum_2.clicked.connect(self.modificar_buscar_inusmo)
    #self.ui.pushButton_Modificar_Inusmo.clicked.connect(self.modificar_insumo)

#---------------------------------------REGISTRO de EMPELADOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def registrar_empleado(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar el empleado?",
                                      QMessageBox.Yes | QMessageBox.No)
    
    if respuesta == QMessageBox.Yes:
      try:
        #Conectar a la base de datos
        conn = sqlite3.connect("C:\\Users\\Ale\\Documents\\GitHub\\SPVCM\\DataBase.db")
        cursor = conn.cursor()

         # Obtener los valores de los campos de entrada


      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el empleado: {str(e)}")
      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
#---------------------------------------REGISTRO de INSUMOS en la BASE DE DATOS-----------------------------------------------------
    self.ui.pushButton_Registrar_Inusmo.clicked.connect(self.registrar_inusmo)
  @Slot()
  def registrar_inusmo(self):
      # Mostrar un mensaje de confirmación
      respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar el insumo?",
                                        QMessageBox.Yes | QMessageBox.No)
      
      if respuesta == QMessageBox.Yes:
          try:
              # Conectar a la base de datos
              conn = sqlite3.connect("C:\\Users\\Ale\\Documents\\GitHub\\SPVCM\\DataBase.db")
              cursor = conn.cursor()

              # Obtener los valores de los campos de entrada
              nombre = self.ui.lineEdit_Nombre_Insumo.text()
              existencia = self.ui.SpinBoxExistencia.value()
              descripcion = self.ui.textEdit_Descripcion.toPlainText()

              # Insertar los valores en la tabla Insumo
              cursor.execute("INSERT INTO Insumo (nombre, existencia, descripcion) VALUES (?, ?, ?)", (nombre, existencia, descripcion))

              # Confirmar la inserción
              conn.commit()

              # Mostrar un mensaje de éxito
              QMessageBox.information(self, "Registro exitoso", "El insumo se ha registrado correctamente.")

          except sqlite3.Error as e:
              # Mostrar un mensaje de error si ocurre un problema
              QMessageBox.critical(self, "Error", f"Error al registrar el insumo: {str(e)}")

          finally:
              # Cerrar la conexión a la base de datos
              conn.close()
#---------------------------------------BUSQUEDA por ID de INSUMOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def buscar_insumo(self):
      try:
          id_insumo = self.ui.lineEdit_Buscar_Insumo.text()
          # Conectar a la base de datos
          conn = sqlite3.connect("C:\\Users\\Ale\\Documents\\GitHub\\SPVCM\\DataBase.db")
          cursor = conn.cursor()

          # Consulta para obtener los datos del insumo por su ID
          cursor.execute("SELECT * FROM Insumo WHERE id = ?", (id_insumo,))
          insumo = cursor.fetchone()  # Obtener el primer resultado

          # Mostrar los datos en la tabla
          if insumo:
            # Limpiar la tabla
            self.ui.tabla_Buscar_Insumo.clearContents()

            # Mostrar los datos del insumo en la tabla
            self.ui.tabla_Buscar_Insumo.setColumnCount(4) #Config. numero de columnas
            self.ui.tabla_Buscar_Insumo.setRowCount(1) #Config. numero de Filas
            headers = ["ID","NOMBRE","EXISTENCIA","DESCRIPCION"]
            self.ui.tabla_Buscar_Insumo.setHorizontalHeaderLabels(headers)  #Headers de Columnas
            # Ocultar los números de las filas
            self.ui.tabla_Buscar_Insumo.verticalHeader().setVisible(False)

            id_widget = QTableWidgetItem(str(insumo[0]))
            nombre_widget = QTableWidgetItem(insumo[1])
            existencia_widget = QTableWidgetItem(str(insumo[2]))
            descripcion_widget = QTableWidgetItem(insumo[3])

            # Centrar el contenido de las celdas
            id_widget.setTextAlignment(Qt.AlignCenter)
            nombre_widget.setTextAlignment(Qt.AlignCenter)
            existencia_widget.setTextAlignment(Qt.AlignCenter)
            descripcion_widget.setTextAlignment(Qt.AlignCenter)

            self.ui.tabla_Buscar_Insumo.setItem(0,0,id_widget)
            self.ui.tabla_Buscar_Insumo.setItem(0,1,nombre_widget)
            self.ui.tabla_Buscar_Insumo.setItem(0,2,existencia_widget)
            self.ui.tabla_Buscar_Insumo.setItem(0,3,descripcion_widget)

            # Ajustar el ancho de las columnas al contenido
            for i in range(self.ui.tabla_Buscar_Insumo.columnCount()):
                self.ui.tabla_Buscar_Insumo.resizeColumnToContents(i)
            
                
          else:
              # Si no se encuentra el insumo, mostrar un mensaje
              QMessageBox.warning(self, "Insumo no encontrado", "No se encontró un insumo con el ID especificado.")

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al buscar el insumo: {str(e)}")

      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
#---------------------------------------Consulta de INSUMOS en la BASE DE DATOS-----------------------------------------------------

#---------------------------------------Modificar INSUMOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def modificar_buscar_inusmo(self):
    id_insumo = self.ui.lineEdit_Buscar_Insumo.text()
    insumo = buscar_insumo(self,id_insumo)
    self.ui.ID_Modificar_Insumo.setText(str(insumo[0]))
    self.ui.lineEdit_Nombre_Insumo_2.setText(str(insumo[1]))
    self.ui.SpinBox_Existencia_2.setValue(int(insumo[2]))
    self.ui.textEdit_Descripcion_2.setText(str(insumo[3]))
    @Slot()
    def modificar_inusmo(self):
        # Mostrar un mensaje de confirmación
        respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea modificar el insumo?",
                                          QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            try:
                # Conectar a la base de datos
                conn = sqlite3.connect("C:\\Users\\Ale\\Documents\\GitHub\\SPVCM\\DataBase.db")
                cursor = conn.cursor()

                # Obtener los valores de los campos de entrada
                nombre = self.ui.lineEdit_Nombre_Insumo_2.text()
                existencia = self.ui.SpinBox_Existencia_2.value()
                descripcion = self.ui.textEdit_Descripcion_2.toPlainText()

                # Modificar los valores en la tabla Insumo
                cursor.execute("UPDATE Insumo SET nombre=?, existencia=?, descripcion=? WHERE id=?", 
                              (nombre, existencia, descripcion, id_insumo))

                # Confirmar la modificación
                conn.commit()

                # Mostrar un mensaje de éxito
                QMessageBox.information(self, "Modificación exitosa", "El insumo se ha modificado correctamente.")

            except sqlite3.Error as e:
                # Mostrar un mensaje de error si ocurre un problema
                QMessageBox.critical(self, "Error", f"Error al registrar el empleado: {str(e)}")
            finally:
                # Cerrar la conexión a la base de datos
                conn.close()
  @Slot()
  def navegar_inicio(self):
    self.stackedWidget.setCurrentIndex(0)
  @Slot()
  def navegar_comandas(self):
    self.stackedWidget.setCurrentIndex(1)
    self.ui.tab_Comandas.setCurrentIndex(0)
  @Slot()
  def navegar_compras(self):
    self.stackedWidget.setCurrentIndex(2)
    self.ui.tab_Compras.setCurrentIndex(0)
  @Slot()
  def navegar_platillos(self):
    self.stackedWidget.setCurrentIndex(3)
    self.ui.tab_Platillos.setCurrentIndex(0)
  @Slot()
  def navegar_insumos(self):
    self.stackedWidget.setCurrentIndex(4)
    self.ui.tab_Insumo.setCurrentIndex(0) 

    next_id = get_cont_insumo(self)
    next_id += 1
    self.ui.ID_Insumo.setText(str(next_id))
  @Slot()
  def navegar_empleados(self):
    self.stackedWidget.setCurrentIndex(5)
    self.ui.tab_Empleados.setCurrentIndex(0)
  @Slot()
  def navegar_provedores(self):
    self.stackedWidget.setCurrentIndex(6)
    self.ui.tab_Provedores.setCurrentIndex(0)




