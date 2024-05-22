from PySide2.QtWidgets import QMainWindow,QMessageBox, QTableWidgetItem, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import sqlite3
from Metodos import *
from datetime import datetime
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

    self.ui.pushButton_Registrar_Proveedor.clicked.connect(self.registrar_proveedor)
      #REGISTROS de 1 a *
    self.ui.pushButton_Registrar_Platillo.clicked.connect(self.registrar_platillo)
    self.ui.pushButton_Buscar_Insumos_ID.clicked.connect(self.buscar_inusmos_platillo)
    self.ui.pushButton_Agregar_Insumo.clicked.connect(self.agregar_Insumo_Tabla)

    self.ui.pushButton_Registrar_Comanda.clicked.connect(self.registrar_comanda)
    self.ui.pushButton_Buscar_Platillos_Comanda.clicked.connect(self.buscar_platillo_comanda)
    self.ui.pushButton_Agregar_Platillos_Comanda.clicked.connect(self.agregar_platillo_tabla)
    
    #BUSQUEDA de datos en la Base de Datos
    self.ui.pushButton_Buscar_Insumo.clicked.connect(self.buscar_insumo)

    self.ui.pushButton_Buscar_Empleado.clicked.connect(self.buscar_empleado)

    self.ui.pushButton_Buscar_Proveedor.clicked.connect(self.buscar_proveedor)

      #ENTIDADES 1 *N
    self.ui.pushButton_Buscar_Platillo.clicked.connect(self.buscar_platillo)

    self.ui.pushButton_Buscar_Comanda.clicked.connect(self.buscar_comanda)
    #CONSULTAR datos en la Base de Datos
    self.ui.pushButton_Mostrar_Insumos.clicked.connect(self.mostrar_insumos)
    
    self.ui.pushButton_Mostrar_Proveedor.clicked.connect(self.mostrar_proveedor)

    self.ui.pushButton_Mostrar_Empleado.clicked.connect(self.mostrar_empleados)

      #ENTIDADES 1 *N
    self.ui.pushButton_Mostrar_Platillos.clicked.connect(self.mostrar_platillos)
    #MODIFICAR datos en la Base de Datos
    self.ui.pushButton_Buscar_Insum_2.clicked.connect(self.modificar_buscar_inusmo)
    self.ui.pushButton_Modificar_Inusmo.clicked.connect(self.modificar_inusmo)

    self.ui.pushButton_Buscar_Empleado_m.clicked.connect(self.modificar_buscar_empleado)
    self.ui.pushButton_Modificar_Empleado.clicked.connect(self.modificar_empleado)

    self.ui.pushButton_Buscar_Proveedor_m.clicked.connect(self.modificar_buscar_proveedor)
    self.ui.pushButton_Modificar_Proveedor.clicked.connect(self.modificar_proveedor)  

#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((COMANDAS))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#---------------------------------------REGISTRO de COMANDAS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def registrar_comanda(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar la Comanda?",
                                      QMessageBox.Yes | QMessageBox.No)
    
    if respuesta == QMessageBox.Yes and self.ui.tabla_Platillos.rowCount:
      try:
        #Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

        # Obtener los valores de los campos de entrada
        estatus = self.ui.comboBox_Estatus_Comanda.currentText()
        fecha = self.ui.fecha_comanda.text()
        # Insertar los valores en la tabla Insumo
        cursor.execute("INSERT INTO Comanda (estatus, fecha) VALUES (?, ?)", 
                      (estatus, fecha))
        # Confirmar la inserción
        conn.commit()
#INSERT EN TABLA 1 a *
        id_comanda = int(self.ui.ID_Comanda.text())
        
        num_filas = self.ui.tabla_Platillos.rowCount()
        for i in range(num_filas):
          id_platillo = itemToInt(self.ui.tabla_Platillos.item(i,0))
          cantidad = itemToFloat(self.ui.tabla_Platillos.item(i,2))
          precio = itemToFloat(self.ui.tabla_Platillos.item(i,3))
          
          cursor.execute("INSERT INTO Platillo_Comanda (id_platillo, id_comanda, cantidad, precio) VALUES (?, ?, ?, ?)", 
                  (id_platillo, id_comanda, cantidad, precio))
          conn.commit()
          
        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro exitoso", "La COMANDA se ha registrado correctamente.")        

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar la Comanda: {str(e)}")
      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
          self.ui.Label_Nombre_Platillo_Comanda.clear()
          self.ui.Label_Precio_Platillo_Comanda.clear()
          self.ui.Label_Descripcion_Platillo_Comanda.clear()
          self.ui.lineEdit_ID_Platillo.clear()

          self.ui.tabla_Platillos.clear()
          self.ui.tabla_Platillos.setRowCount(0)
          self.ui.tabla_Platillos.setColumnCount(0)

          self.ui.Subtotal.clear()
          self.ui.IVA.clear()
          self.ui.Total.clear()
          
          #self.ui.ID_Comanda.setText(str(get_cont_comanda(self)+1))

    else:
      if respuesta != QMessageBox.No:
          QMessageBox.critical(self, "Error", "No hay informacion suficiente para registrar el Platillo .")
  @Slot()
  def buscar_platillo_comanda(self): 
      try:
          id_platillo = self.ui.lineEdit_ID_Platillo.text()
          # Conectar a la base de datos
          platillo = buscar_platillo(self,id_platillo)

          # Mostrar los datos en la tabla
          if platillo:
            # Limpiar la labels
            self.ui.Label_Nombre_Platillo_Comanda.clear()
            self.ui.Label_Precio_Platillo_Comanda.clear()
            self.ui.Label_Descripcion_Platillo_Comanda.clear()

            #Mostrar Datos de Insumo en LABELS
            self.ui.Label_Nombre_Platillo_Comanda.setText(platillo[1])
            self.ui.Label_Precio_Platillo_Comanda.setText(str(platillo[2]))
            self.ui.Label_Descripcion_Platillo_Comanda.setText(platillo[3])

            self.ui.pushButton_Agregar_Platillos_Comanda.show()
          else:
              # Si no se encuentra el Insumo, mostrar un mensaje
              QMessageBox.warning(self, "Platillo no encontrado", "No se encontró un Platillo con el ID especificado.")

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al buscar el Platillo: {str(e)}")       
  @Slot()
  def agregar_platillo_tabla(self):
    tasa_iva = 0.16
    id_platillo = self.ui.lineEdit_ID_Platillo.text()
    # Conectar a la base de datos
    platillo = buscar_platillo(self,id_platillo)

    # Mostrar los datos en la tabla
    if platillo:
      # Mostrar Encabezados en la tabla
      self.ui.tabla_Platillos.setColumnCount(5) #Config. numero de columnas
      headers = ["ID", "NOMBRE", "CANTIDAD", "PRECIO", "IMPORTE"]
      self.ui.tabla_Platillos.setHorizontalHeaderLabels(headers)  #Headers de Columnas

      # Ocultar los números de las filas
      self.ui.tabla_Platillos.verticalHeader().setVisible(False) 


      num_filas = self.ui.tabla_Platillos.rowCount()
      fila_encontrado = -1
      cantidad = self.ui.spinBox_Cantidad_Platillo.value()
      encontrado = False
      precio = platillo[2]
      # Buscar ID en la tabla
      for i in range (num_filas): 
        id_actual_item = self.ui.tabla_Platillos.item(i,0).text()
        id_actual = str(id_actual_item)
        if(id_actual == id_platillo):
            fila_encontrado = i
            encontrado = True
            break
      if (encontrado): # Si se ecnontro el platillo
        #obtener cantidad actual 
        cantidad_actual_item = self.ui.tabla_Platillos.item(fila_encontrado,2)
        cantidad_actual = itemToFloat(cantidad_actual_item)

        # cantidad a Item
        nueva_cantidad = cantidad_actual + cantidad
        importe = nueva_cantidad * precio

        nueva_cantidad_widget = QTableWidgetItem(str(nueva_cantidad))
        importe_widget = QTableWidgetItem(str(importe))

        nueva_cantidad_widget.setTextAlignment(Qt.AlignCenter)
        importe_widget.setTextAlignment(Qt.AlignCenter)
        #Actualizar cantidad
        self.ui.tabla_Platillos.setItem(fila_encontrado,2,nueva_cantidad_widget)
        self.ui.tabla_Platillos.setItem(fila_encontrado,4,importe_widget)
      else:  #Si NO se encontro el ID
        self.ui.tabla_Platillos.insertRow(num_filas)
        importe = cantidad * precio

        id_widget = QTableWidgetItem(str(platillo[0]))
        nombre_widget = QTableWidgetItem(platillo[1])
        cantidad_widget = QTableWidgetItem(str(cantidad))
        precio_widget = QTableWidgetItem(str(platillo[2]))
        importe_widget = QTableWidgetItem(str(importe))

        # Centrar el contenido de las celdas
        id_widget.setTextAlignment(Qt.AlignCenter)
        nombre_widget.setTextAlignment(Qt.AlignCenter)
        cantidad_widget.setTextAlignment(Qt.AlignCenter)
        precio_widget.setTextAlignment(Qt.AlignCenter)
        importe_widget.setTextAlignment(Qt.AlignCenter)

        self.ui.tabla_Platillos.setItem(num_filas,0,id_widget)
        self.ui.tabla_Platillos.setItem(num_filas,1,nombre_widget)
        self.ui.tabla_Platillos.setItem(num_filas,2,cantidad_widget)
        self.ui.tabla_Platillos.setItem(num_filas,3,precio_widget)
        self.ui.tabla_Platillos.setItem(num_filas,4,importe_widget)

        num_filas += 1
        
      # ACTUALIZAR LABLES CALCULABLES
      self.ui.spinBox_Cantidad_Platillo.setValue(0)
      #calcular SUBTOTAL
      subtotal = 0
      if not num_filas:
         subtotal = cantidad * precio
      for i in range (num_filas): 
          importe_i_index = self.ui.tabla_Platillos.item(i,4)
          importe_i= itemToFloat(importe_i_index)
          subtotal += importe_i
      #calcular IVA
      iva = subtotal * tasa_iva
      #calcular TOTAL
      total = subtotal + iva 

      self.ui.Subtotal.setText(str(round(subtotal,2)))
      self.ui.IVA.setText(str(round(iva,2)))
      self.ui.Total.setText(str(round(total,2)))   
    else:
      # Si no se encuentra el Platillo, mostrar un mensaje
      QMessageBox.warning(self, "Platillo no encontrado", "No se encontró un Insumo con el ID especificado.")


#---------------------------------------BUSCAR de COMANDASen la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def buscar_comanda(self):
        try:
            id_comanda = self.ui.lineEdit_ID_Buscar_Comanda.text()
            # Conectar a la base de datos
            comanda = buscar_comanda(self,id_comanda)
            tasa_iva = 0.16

            # Mostrar los datos en la tabla
            if comanda:
              self.ui.fecha_buscar_comadna.setText(comanda[2])
              # Limpiar la tabla
              self.ui.Label_Estatus_Comanda_Buscar.clear()
              
              self.ui.tabla_Buscar_Platillos.clear()
              self.ui.tabla_Buscar_Platillos.setRowCount(0)
              self.ui.tabla_Buscar_Platillos.setColumnCount(0)

              # Mostrar los datos de la COMANDA en la tabla
              self.ui.Esatus_Platillo.setText(comanda[1])

              #Obtener PLATILLOS
              conn = connect_db()
              cursor = conn.cursor()
              cursor.execute(
              """SELECT P.id, P.nombre, PC.cantidad, PC.precio 
                FROM Platillo P
                JOIN Platillo_Comanda PC ON P.id = PC.id_platillo
                JOIN Comanda  C ON PC.id_comanda = C.id
                WHERE C.id = ?;""", (id_comanda))
              platillos = cursor.fetchall()
              conn.close()

              headers = ["ID", "NOMBRE", "CANTIDAD", "PRECIO", "IMPORTE"]
              self.ui.tabla_Buscar_Platillos.setColumnCount(len(headers)) #Config. numero de columnas
              self.ui.tabla_Buscar_Platillos.setHorizontalHeaderLabels(headers)  #Headers de Columnas
            
              # Ocultar los números de las filas
              self.ui.tabla_Buscar_Platillos.verticalHeader().setVisible(False)

              subtotal=0

              for i, platillo in enumerate(platillos):
                  self.ui.tabla_Buscar_Platillos.insertRow(i)
                  for j, valor in enumerate(platillo):
                      item = QTableWidgetItem(str(valor))
                      item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto en la celda
                      self.ui.tabla_Buscar_Platillos.setItem(i,j,item)
                  importe = platillo[2]* platillo[3]
                  importe_item = QTableWidgetItem(str(importe))
                  self.ui.tabla_Buscar_Platillos.setItem(i,4,importe_item)
                  subtotal += importe
              for i in range(self.ui.tabla_Buscar_Platillos.columnCount()):
                self.ui.tabla_Buscar_Platillos.resizeColumnToContents(i)
              iva = round(subtotal*tasa_iva,2)
              total = round(subtotal + iva,2)
              self.ui.Subtotal_2.setText(str(round(subtotal,2)))
              self.ui.IVA_2.setText(str(iva))
              self.ui.Total_2.setText(str(total))
            else:
              # Si no se encuentra el Empleado, mostrar un mensaje
              QMessageBox.warning(self, "Comanda no encontrada", "No se encontró una Comanda con el ID especificado.")

        except sqlite3.Error as e:
            # Mostrar un mensaje de error si ocurre un problema
            QMessageBox.critical(self, "Error", f"Error al buscar la Comanda: {str(e)}")


#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((PLATILLOS))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#---------------------------------------REGISTRO de PLATILLOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def registrar_platillo(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar el Platillo?",
                                      QMessageBox.Yes | QMessageBox.No)
    
    if respuesta == QMessageBox.Yes and self.ui.lineEdit_Nombre_Platillo.text():
      try:
        #Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

        # Obtener los valores de los campos de entrada
        nombre = self.ui.lineEdit_Nombre_Platillo.text()
        precio = self.ui.SpinBox_Precio_Platillo.value()
        descripcion = self.ui.lineEdit_Descripcion_Platillo.text()
        estatus = self.ui.comboBox_Estatus_Proveedor.currentText()
        # Insertar los valores en la tabla Insumo
        cursor.execute("INSERT INTO Platillo (nombre, precio, descripcion,estatus) VALUES (?, ?, ?, ?)", 
                      (nombre, precio , descripcion,estatus))
        # Confirmar la inserción
        conn.commit()
#INSERT EN TABLA 1 a *
        id_platillo = int(self.ui.ID_Platillo.text())
        
        num_filas = self.ui.tabla_Buscar_Insumos_Platillo.rowCount()
        for i in range(num_filas):
          id_insumo = itemToInt(self.ui.tabla_Buscar_Insumos_Platillo.item(i,0))
          cantidad = itemToFloat(self.ui.tabla_Buscar_Insumos_Platillo.item(i,2))
          
          cursor.execute("INSERT INTO Insumos_Platillo (id_insumo, id_platillo, cantidad) VALUES (?, ?, ?)", 
                  (id_insumo, id_platillo ,cantidad))
          conn.commit()
          
        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro exitoso", "El Platillo se ha registrado correctamente.")        

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el Platillo: {str(e)}")
      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
          self.ui.lineEdit_Nombre_Platillo.clear()
          self.ui.SpinBox_Precio_Platillo.clear()
          self.ui.lineEdit_Descripcion_Platillo.clear()
          self.ui.lineEdit_ID_Insumos_Platillo.clear()
          self.ui.Label_Nombre_Insumo.clear()
          self.ui.Label_Descripcion_Insumo.clear()
          self.ui.SpinBox_Cantidad_Insumo.clear()
          self.ui.tabla_Buscar_Insumos_Platillo.setRowCount(0)
          self.ui.ID_Platillo.setText(str(get_cont_platillos(self)+1))

    else:
      if respuesta != QMessageBox.No:
          QMessageBox.critical(self, "Error", "No hay informacion suficiente para registrar el Platillo .")
  @Slot()
  def buscar_inusmos_platillo(self): 
      try:
          id_insumo = self.ui.lineEdit_ID_Insumos_Platillo.text()
          # Conectar a la base de datos
          insumo = buscar_insumo(self,id_insumo)

          # Mostrar los datos en la tabla
          if insumo:
            # Limpiar la labels
            self.ui.Label_Nombre_Insumo.clear()
            self.ui.Label_Descripcion_Insumo.clear()

            #Mostrar Datos de Insumo en LABELS
            self.ui.Label_Nombre_Insumo.setText(str(insumo[1]))
            self.ui.Label_Descripcion_Insumo.setText(str(insumo[3]))
            self.ui.pushButton_Agregar_Insumo.show()
          else:
              # Si no se encuentra el Insumo, mostrar un mensaje
              QMessageBox.warning(self, "Insumo no encontrado", "No se encontró un Insumo con el ID especificado.")

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al buscar el Insumo: {str(e)}")             
  @Slot()
  def agregar_Insumo_Tabla(self):
    id_insumo = self.ui.lineEdit_ID_Insumos_Platillo.text()
    # Conectar a la base de datos
    insumo = buscar_insumo(self,id_insumo)

    # Mostrar los datos en la tabla
    if insumo:
      # Mostrar Encabezados en la tabla
      self.ui.tabla_Buscar_Insumos_Platillo.setColumnCount(4) #Config. numero de columnas
      headers = ["ID", "NOMBRE", "CANTIDAD", "DESCRIPCIÓN"]
      self.ui.tabla_Buscar_Insumos_Platillo.setHorizontalHeaderLabels(headers)  #Headers de Columnas

      # Ocultar los números de las filas
      self.ui.tabla_Buscar_Insumos_Platillo.verticalHeader().setVisible(False) 

      id_insumo = self.ui.lineEdit_ID_Insumos_Platillo.text()
      num_filas = self.ui.tabla_Buscar_Insumos_Platillo.rowCount()
      fila_encontrado = -1
      cantidad = self.ui.SpinBox_Cantidad_Insumo.value()
      encontrado = False
      # Buscar ID en la tabla
      for i in range (num_filas): 
        id_actual_item = self.ui.tabla_Buscar_Insumos_Platillo.item(i,0).text()
        id_actual = str(id_actual_item)
        if(id_actual == id_insumo):
            fila_encontrado = i
            encontrado = True
            break
      if (encontrado): # Si se ecnontro el insumo
        #obtener cantidad actual 
        cantidad_actual_item = self.ui.tabla_Buscar_Insumos_Platillo.item(fila_encontrado,2)
        cantidad_actual_texto = cantidad_actual_item.text()
        cantidad_actual = float(cantidad_actual_texto)

        # cantidad a Item
        nueva_cantidad = cantidad_actual + cantidad

        nueva_cantidad_widget = QTableWidgetItem(str(nueva_cantidad))
        nueva_cantidad_widget.setTextAlignment(Qt.AlignCenter)
        #Actualizar cantidad
        self.ui.tabla_Buscar_Insumos_Platillo.setItem(fila_encontrado,2,nueva_cantidad_widget)
      else:  #Si NO se encontro el ID
        self.ui.tabla_Buscar_Insumos_Platillo.insertRow(num_filas)

        id_widget = QTableWidgetItem(str(insumo[0]))
        nombre_widget = QTableWidgetItem(insumo[1])
        cantidad_widget = QTableWidgetItem(str(cantidad))
        descripcion_widget = QTableWidgetItem(insumo[3])

        # Centrar el contenido de las celdas
        id_widget.setTextAlignment(Qt.AlignCenter)
        nombre_widget.setTextAlignment(Qt.AlignCenter)
        cantidad_widget.setTextAlignment(Qt.AlignCenter)
        descripcion_widget.setTextAlignment(Qt.AlignCenter)

        self.ui.tabla_Buscar_Insumos_Platillo.setItem(num_filas,0,id_widget)
        self.ui.tabla_Buscar_Insumos_Platillo.setItem(num_filas,1,nombre_widget)
        self.ui.tabla_Buscar_Insumos_Platillo.setItem(num_filas,2,cantidad_widget)
        self.ui.tabla_Buscar_Insumos_Platillo.setItem(num_filas,3,descripcion_widget)
      self.ui.SpinBox_Cantidad_Insumo.setValue(0)
    else:
      # Si no se encuentra el Insumo, mostrar un mensaje
      QMessageBox.warning(self, "Insumo no encontrado", "No se encontró un Insumo con el ID especificado.")
#---------------------------------------BUSCAR de PLATILLOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def buscar_platillo(self):
      try:
          id_platillo = self.ui.lineEdit_ID_Buscar_Platillo.text()
          # Conectar a la base de datos
          platillo = buscar_platillo(self,id_platillo)

          # Mostrar los datos en la tabla
          if platillo:
            # Limpiar la tabla
            self.ui.Nombre_Platillo.clear()
            self.ui.Precio_Platillo.clear()
            self.ui.Descripcion_Platillo.clear()
            self.ui.Esatus_Platillo.clear()
            
            self.ui.tabla_Buscar_Insumos_Platillo_2.clearContents()

            # Mostrar los datos del Proveedor en la tabla
            self.ui.Nombre_Platillo.setText(platillo[1])
            self.ui.Precio_Platillo.setText(str(platillo[2]))
            self.ui.Descripcion_Platillo.setText(platillo[3])
            self.ui.Esatus_Platillo.setText(platillo[4])

            #Obtener INSUMOS del
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(
            """SELECT I.id, I.nombre, IP.cantidad
                FROM Insumo I
                JOIN Insumos_Platillo IP ON I.id = IP.id_insumo
                JOIN Platillo P ON IP.id_platillo = P.id
                WHERE P.id = ? """, (id_platillo))
            insumos = cursor.fetchall()
            conn.close()

            
            self.ui.tabla_Buscar_Insumos_Platillo_2.setColumnCount(3) #Config. numero de columnas
            headers = ["ID", "NOMBRE", "CANTIDAD"]
            self.ui.tabla_Buscar_Insumos_Platillo_2.setHorizontalHeaderLabels(headers)  #Headers de Columnas
          
            # Ocultar los números de las filas
            self.ui.tabla_Buscar_Insumos_Platillo_2.verticalHeader().setVisible(False)


            for i, insumo in enumerate(insumos):
                self.ui.tabla_Buscar_Insumos_Platillo_2.insertRow(i)
                for j, valor in enumerate(insumo):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto en la celda
                    self.ui.tabla_Buscar_Insumos_Platillo_2.setItem(i,j,item)        
            for i in range(self.ui.tabla_Buscar_Insumos_Platillo_2.columnCount()):
              self.ui.tabla_Buscar_Insumos_Platillo_2.resizeColumnToContents(i)
          else:
              # Si no se encuentra el Empleado, mostrar un mensaje
              QMessageBox.warning(self, "Platillo no encontrado", "No se encontró un Platillo con el ID especificado.")

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al buscar el Platillo: {str(e)}")

#---------------------------------------CONSULTAR de PLATILLOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def mostrar_platillos(self):
    try:
        # Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

        # Obtener todos los Platillos
        cursor.execute("SELECT * FROM Platillo")
        platillos = cursor.fetchall()

        self.ui.tabla_Consultar_Platillos.clearContents()
        # Mostrar los Platillos en la tabla
        self.ui.tabla_Consultar_Platillos.setRowCount(len(platillos))
        headers = ["ID","NOMBRE","PRECIO","DESCRIPCION","ESTATUS"]
        self.ui.tabla_Consultar_Platillos.setColumnCount(len(headers))
        self.ui.tabla_Consultar_Platillos.setHorizontalHeaderLabels(headers)
        self.ui.tabla_Consultar_Platillos.verticalHeader().setVisible(False)
        # Ajustar el tamaño de los encabezados al contenido
        header = self.ui.tabla_Consultar_Platillos.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        for i, platillo in enumerate(platillos):
            for j, valor in enumerate(platillo):
                item = QTableWidgetItem(str(valor))
                item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto en la celda
                self.ui.tabla_Consultar_Platillos.setItem(i, j, item)
                    # Ajustar el ancho de las columnas al contenido
            for i in range(self.ui.tabla_Buscar_Platillos.columnCount()):
                self.ui.tabla_Buscar_Platillos.resizeColumnToContents(i)

    except sqlite3.Error as e:
        # Mostrar un mensaje de error si ocurre un problema
        QMessageBox.critical(self, "Error", f"Error al mostrar los Platillos: {str(e)}")
    finally:
        # Cerrar la conexión a la base de datos
        conn.close()

#---------------------------------------MODIFICAR de PLATILLOS en la BASE DE DATOS-----------------------------------------------------



#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((PROVEDORES))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))



#---------------------------------------REGISTRO de PROVEEDORES en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def registrar_proveedor(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar el Proveedor?",
                                      QMessageBox.Yes | QMessageBox.No)
    
    if respuesta == QMessageBox.Yes and self.ui.lineEdit_Nombre_Proveedor.text():
      try:
        #Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

         # Obtener los valores de los campos de entrada
        nombre = self.ui.lineEdit_Nombre_Proveedor.text()
        telefono = self.ui.lineEdit_Telefono_Proveedor.text()
        estatus = self.ui.comboBox_Estatus_Proveedor.currentText()
        # Insertar los valores en la tabla Insumo
        cursor.execute("INSERT INTO Proveedor (nombre, telefono, estatus) VALUES (?, ?, ?)", (nombre,telefono,estatus))

        # Confirmar la inserción
        conn.commit()

        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro exitoso", "El Proveedor se ha registrado correctamente.")        

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el Proveedor: {str(e)}")
      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
          self.ui.lineEdit_Nombre_Proveedor.clear()
          self.ui.lineEdit_Telefono_Proveedor.clear()
          self.ui.ID_Proveedor.setText(str(get_cont_proveedor(self)+1))

    else:
       if respuesta != QMessageBox.No:
          QMessageBox.critical(self, "Error", "No hay informacion suficiente paraq registrar el Proveedor .")
#---------------------------------------BUSQUEDA por ID de PROVEEDORES en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def buscar_proveedor(self):
      try:
          id_proveedor = self.ui.lineEdit_Buscar_Proveedor.text()
          # Conectar a la base de datos
          proveedor = buscar_proveedor(self,id_proveedor)

          # Mostrar los datos en la tabla
          if proveedor:
            # Limpiar la tabla
            self.ui.tabla_Buscar_Proveedor.clearContents()

            # Mostrar los datos del Proveedor en la tabla
            self.ui.tabla_Buscar_Proveedor.setColumnCount(4) #Config. numero de columnas
            self.ui.tabla_Buscar_Proveedor.setRowCount(1) #Config. numero de Filas
            headers = ["ID","NOMBRE","TELEFONO","ESTATUS"]
            self.ui.tabla_Buscar_Proveedor.setHorizontalHeaderLabels(headers)  #Headers de Columnas
            # Ocultar los números de las filas
            self.ui.tabla_Buscar_Proveedor.verticalHeader().setVisible(False)

            id_widget = QTableWidgetItem(str(proveedor[0]))
            nombre_widget = QTableWidgetItem(proveedor[1])
            telefono_widget = QTableWidgetItem(proveedor[2])
            estatus_widget = QTableWidgetItem(proveedor[3])

            # Centrar el contenido de las celdas
            id_widget.setTextAlignment(Qt.AlignCenter)
            nombre_widget.setTextAlignment(Qt.AlignCenter)
            telefono_widget.setTextAlignment(Qt.AlignCenter)
            estatus_widget.setTextAlignment(Qt.AlignCenter)

            self.ui.tabla_Buscar_Proveedor.setItem(0,0,id_widget)
            self.ui.tabla_Buscar_Proveedor.setItem(0,1,nombre_widget)
            self.ui.tabla_Buscar_Proveedor.setItem(0,2,telefono_widget)
            self.ui.tabla_Buscar_Proveedor.setItem(0,3,estatus_widget)

            # Ajustar el ancho de las columnas al contenido
            for i in range(self.ui.tabla_Buscar_Proveedor.columnCount()):
                self.ui.tabla_Buscar_Proveedor.resizeColumnToContents(i)
            
                
          else:
              # Si no se encuentra el Empleado, mostrar un mensaje
              QMessageBox.warning(self, "Proveedor no encontrado", "No se encontró un Proveedor con el ID especificado.")

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al buscar el Proveedor: {str(e)}")
#---------------------------------------Consulta de PROVEEDORES en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def mostrar_proveedor(self):
    try:
        # Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

        # Obtener todos los Proveedores
        cursor.execute("SELECT * FROM Proveedor")
        proveedores = cursor.fetchall()

        # Mostrar los Proveedores en la tabla
        self.ui.tabla_Consultar_Proveedor.clearContents()
        self.ui.tabla_Consultar_Proveedor.setRowCount(len(proveedores))
        headers = ["ID","NOMBRE","TELEFONO","ESTATUS"]
        self.ui.tabla_Consultar_Proveedor.setColumnCount(len(headers))
        self.ui.tabla_Consultar_Proveedor.setHorizontalHeaderLabels(headers)
        self.ui.tabla_Consultar_Proveedor.verticalHeader().setVisible(False)
        # Ajustar el tamaño de los encabezados al contenido
        header = self.ui.tabla_Consultar_Proveedor.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        for i, proveedor in enumerate(proveedores):
            for j, valor in enumerate(proveedor):
                item = QTableWidgetItem(str(valor))
                item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto en la celda
                self.ui.tabla_Consultar_Proveedor.setItem(i, j, item)
                    # Ajustar el ancho de las columnas al contenido
            for i in range(self.ui.tabla_Buscar_Proveedor.columnCount()):
                self.ui.tabla_Buscar_Proveedor.resizeColumnToContents(i)

    except sqlite3.Error as e:
        # Mostrar un mensaje de error si ocurre un problema
        QMessageBox.critical(self, "Error", f"Error al mostrar los Proveedor: {str(e)}")
    finally:
        # Cerrar la conexión a la base de datos
        conn.close()
#---------------------------------------Modificar PROVEEDORES en la BASE DE DATOS----------------------------------------------------- 
  @Slot()
  def modificar_buscar_proveedor(self):
    try:
      id_proveedor= self.ui.lineEdit_Buscar_Proveedor_m.text()
      proveedor = buscar_proveedor(self, id_proveedor)
      if proveedor:
          self.ui.ID_Modficar_Proveedor.setText(str(proveedor[0]))
          self.ui.lineEdit_Nombre_Proveedor_2.setText(str(proveedor[1]))      
          self.ui.lineEdit_Telefono_Proveedor_2.setText(str(proveedor[2]))
          self.ui.comboBox_Estatus_Proveedor_2.setCurrentText(str(proveedor[3]))
      else:
          # Manejar el caso en que no se encuentre el insumo
         QMessageBox.warning(self, "Proveedor no encontrado", "No se encontró un proveedor con el ID especificado.")
    except sqlite3.Error as e:
      # Mostrar un mensaje de error si hay un problema con la base de datos
      print(id_proveedor)  # Para verificar el valor de id_insumo
      QMessageBox.critical(self, "Error", f"Error al buscar el Proveedor con ID {id_proveedor} en la base de datos: {str(e)}")     
    finally:
       self.ui.pushButton_Modificar_Proveedor.show()
 
  @Slot()
  def modificar_proveedor(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea modificar el Proveedor?",
                                      QMessageBox.Yes | QMessageBox.No)
    if respuesta == QMessageBox.Yes:
        try:
          # Conectar a la base de datos
          conn = connect_db()
          cursor = conn.cursor()

          # Obtener los valores de los campos de entrada
          id_proveedor = self.ui.ID_Modficar_Proveedor.text()
          nombre = self.ui.lineEdit_Nombre_Proveedor_2.text()
          telefono = self.ui.lineEdit_Telefono_Proveedor_2.text()
          estatus = self.ui.comboBox_Estatus_Proveedor_2.currentText()
          # Modificar los valores en la tabla Proveedor
          cursor.execute("UPDATE Proveedor SET nombre=?, telefono=?, estatus=? WHERE id=?", 
                        (nombre, telefono, estatus, id_proveedor))

          # Confirmar la modificación
          # Verificar que se haya realizado la actualización correctamente
          if cursor.rowcount > 0:
              # Confirmar la modificación
              conn.commit()
              # Mostrar un mensaje de éxito
              QMessageBox.information(self, "Modificación exitosa", "El Proveedor se ha modificado correctamente.")
          else:
             QMessageBox.critical(self, "Error", "ID de Proveedor no encotrado.")
        except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el Proveedor: {str(e)}")
        finally:
          # Cerrar la conexión a la base de datos
          conn.close()     
          self.ui.lineEdit_Buscar_Proveedor_m.clear()
          self.ui.ID_Modficar_Proveedor.setText("-")
          self.ui.lineEdit_Nombre_Proveedor_2.clear()
          self.ui.lineEdit_Telefono_Proveedor_2.clear()
 
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((EMPLEADOS))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#---------------------------------------REGISTRO de EMPELADOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def registrar_empleado(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar el Empleado?",
                                      QMessageBox.Yes | QMessageBox.No)
    
    if respuesta == QMessageBox.Yes and self.ui.lineEdit_Nombre_Empleado.text():
      try:
        #Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

         # Obtener los valores de los campos de entrada
        nombre = self.ui.lineEdit_Nombre_Empleado.text()
        cargo = self.ui.comboBox_Cargo_Empleado.currentText()
        estatus = self.ui.comboBox_Estatus_Empleado.currentText()
        telefono = self.ui.lineEdit_Telefono_Empleado.text()
        # Insertar los valores en la tabla Insumo
        cursor.execute("INSERT INTO Empleado (nombre, cargo, estatus, telefono) VALUES (?, ?, ?, ?)", (nombre, cargo, estatus,telefono))

        # Confirmar la inserción
        conn.commit()

        # Mostrar un mensaje de éxito
        QMessageBox.information(self, "Registro exitoso", "El Empleado se ha registrado correctamente.")        

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el Empleado: {str(e)}")
      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
          self.ui.lineEdit_Nombre_Empleado.clear()
          self.ui.lineEdit_Telefono_Empleado.clear()
          self.ui.ID_Empleado.setText(str(get_cont_empleado(self)+1))          
    else:
      if respuesta != QMessageBox.No:
        QMessageBox.critical(self, "Error", "No hya informacion suficiente pra registrar el Empleado.")         
#---------------------------------------BUSQUEDA por ID de EMPLEADOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def buscar_empleado(self):
      try:
          id_empleado = self.ui.lineEdit_Buscar_Empleado.text()
          # Conectar a la base de datos
          empleado = buscar_empleado(self,id_empleado)

          # Mostrar los datos en la tabla
          if empleado:
            # Limpiar la tabla
            self.ui.tabla_Buscar_Empleado.clearContents()

            # Mostrar los datos del insumo en la tabla
            self.ui.tabla_Buscar_Empleado.setColumnCount(5) #Config. numero de columnas
            self.ui.tabla_Buscar_Empleado.setRowCount(1) #Config. numero de Filas
            headers = ["ID","NOMBRE","CARGO","ESTATUS","TELEFONO"]
            self.ui.tabla_Buscar_Empleado.setHorizontalHeaderLabels(headers)  #Headers de Columnas
            # Ocultar los números de las filas
            self.ui.tabla_Buscar_Empleado.verticalHeader().setVisible(False)

            id_widget = QTableWidgetItem(str(empleado[0]))
            nombre_widget = QTableWidgetItem(empleado[1])
            cargo_widget = QTableWidgetItem(str(empleado[2]))
            estatus_widget = QTableWidgetItem(empleado[3])
            telefono_widget = QTableWidgetItem(empleado[4])

            # Centrar el contenido de las celdas
            id_widget.setTextAlignment(Qt.AlignCenter)
            nombre_widget.setTextAlignment(Qt.AlignCenter)
            cargo_widget.setTextAlignment(Qt.AlignCenter)
            estatus_widget.setTextAlignment(Qt.AlignCenter)
            telefono_widget.setTextAlignment(Qt.AlignCenter)

            self.ui.tabla_Buscar_Empleado.setItem(0,0,id_widget)
            self.ui.tabla_Buscar_Empleado.setItem(0,1,nombre_widget)
            self.ui.tabla_Buscar_Empleado.setItem(0,2,cargo_widget)
            self.ui.tabla_Buscar_Empleado.setItem(0,3,estatus_widget)
            self.ui.tabla_Buscar_Empleado.setItem(0,4,telefono_widget)

            # Ajustar el ancho de las columnas al contenido
            for i in range(self.ui.tabla_Buscar_Empleado.columnCount()):
                self.ui.tabla_Buscar_Empleado.resizeColumnToContents(i)
            
                
          else:
              # Si no se encuentra el Empleado, mostrar un mensaje
              QMessageBox.warning(self, "Empleado no encontrado", "No se encontró un Empleado con el ID especificado.")

      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al buscar el Empleado: {str(e)}")
#---------------------------------------Consulta de EMPLEADOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def mostrar_empleados(self):
    try:
        # Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor()

        # Obtener todos los insumos
        cursor.execute("SELECT * FROM Empleado")
        empleados = cursor.fetchall()

        # Mostrar los insumos en la tabla
        self.ui.tabla_Consultar_Empleado.clearContents()
        self.ui.tabla_Consultar_Empleado.setRowCount(len(empleados))
        headers = ["ID","NOMBRE","CARGO","ESTATUS","TELEFONO"]
        self.ui.tabla_Consultar_Empleado.setColumnCount(len(headers))
        self.ui.tabla_Consultar_Empleado.setHorizontalHeaderLabels(headers)
        self.ui.tabla_Consultar_Empleado.verticalHeader().setVisible(False)
        # Ajustar el tamaño de los encabezados al contenido
        header = self.ui.tabla_Consultar_Empleado.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        for i, empleado in enumerate(empleados):
            for j, valor in enumerate(empleado):
                item = QTableWidgetItem(str(valor))
                item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto en la celda
                self.ui.tabla_Consultar_Empleado.setItem(i, j, item)
                    # Ajustar el ancho de las columnas al contenido


    except sqlite3.Error as e:
        # Mostrar un mensaje de error si ocurre un problema
        QMessageBox.critical(self, "Error", f"Error al mostrar los Empleados: {str(e)}")
    finally:
        # Cerrar la conexión a la base de datos
        conn.close()
#---------------------------------------Modificar EMPLEADOS en la BASE DE DATOS----------------------------------------------------- 
  @Slot()
  def modificar_buscar_empleado(self):
    try:
      id_empleado= self.ui.lineEdit_Buscar_Empleado_m.text()
      empleado = buscar_empleado(self, id_empleado)
      if empleado:
          self.ui.ID_Modificar_Empleado.setText(str(empleado[0]))
          self.ui.lineEdit_Nombre_Empleado_2.setText(str(empleado[1]))
          self.ui.comboBox_Cargo_Empleado_2.setCurrentText(str(empleado[2]))
          self.ui.comboBox_Estatus_Empleado_2.setCurrentText(str(empleado[3]))
          self.ui.lineEdit_Telefono_Empleado_2.setText(str(empleado[4]))
      else:
          # Manejar el caso en que no se encuentre el insumo
         QMessageBox.warning(self, "Empleado no encontrado", "No se encontró un empleado con el ID especificado.")
    except sqlite3.Error as e:
      # Mostrar un mensaje de error si hay un problema con la base de datos
      print(id_empleado)  # Para verificar el valor de id_insumo
      QMessageBox.critical(self, "Error", f"Error al buscar el Empleado con ID {id_empleado} en la base de datos: {str(e)}")     
    finally:
       self.ui.pushButton_Modificar_Empleado.show()
 
  @Slot()
  def modificar_empleado(self):
    # Mostrar un mensaje de confirmación
    respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea modificar el Empleado?",
                                      QMessageBox.Yes | QMessageBox.No)
    if respuesta == QMessageBox.Yes:
        try:
          # Conectar a la base de datos
          conn = connect_db()
          cursor = conn.cursor()

          # Obtener los valores de los campos de entrada
          id_empleado = self.ui.ID_Modificar_Empleado.text()
          nombre = self.ui.lineEdit_Nombre_Empleado_2.text()
          cargo = self.ui.comboBox_Cargo_Empleado_2.currentText()
          estatus = self.ui.comboBox_Estatus_Empleado_2.currentText()
          telefono = self.ui.lineEdit_Telefono_Empleado_2.text()
          # Modificar los valores en la tabla Empleado
          cursor.execute("UPDATE Empleado SET nombre=?, cargo=?, estatus=?, telefono=? WHERE id=?",
                        (nombre, cargo, estatus,telefono,id_empleado))

          # Confirmar la modificación
          if cursor.rowcount > 0:
            # Confirmar la modificación
            conn.commit()
            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Modificación exitosa", "El Empleado se ha modificado correctamente.")
          else:
              # Mostrar un mensaje de error si no se encontró el ID del proveedor
              QMessageBox.critical(self, "Error", "ID de Empleado no encontrado.")
        except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el empleado: {str(e)}")
        finally:
          # Cerrar la conexión a la base de datos
          conn.close()     
          self.ui.lineEdit_Buscar_Empleado_m.clear()
          self.ui.ID_Modificar_Empleado.setText("-")
          self.ui.ID_Modificar_Empleado.clear()
          self.ui.lineEdit_Nombre_Empleado_2.clear()
          self.ui.lineEdit_Telefono_Empleado_2.clear()
 #(((((((((((((((((((((((((((((((((((((((((((((((((((((((INSUMOS)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#---------------------------------------REGISTRO de INSUMOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def registrar_inusmo(self):
      # Mostrar un mensaje de confirmación
      respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea registrar el insumo?",
                                        QMessageBox.Yes | QMessageBox.No)
      
      if respuesta == QMessageBox.Yes and self.ui.lineEdit_Nombre_Insumo.text():
          try:
              # Conectar a la base de datos
              conn = connect_db()
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
              self.ui.lineEdit_Nombre_Insumo.clear()
              self.ui.SpinBoxExistencia.setValue(0)
              self.ui.textEdit_Descripcion.clear()
              self.ui.ID_Insumo.setText(str(get_cont_insumo(self)+1))
      else:
        if respuesta != QMessageBox.No:
          QMessageBox.critical(self, "Error", "No hay informacion suficiente para registrar el Insumo.")
#---------------------------------------BUSQUEDA por ID de INSUMOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def buscar_insumo(self):
      try:
          id_insumo = self.ui.lineEdit_Buscar_Insumo.text()
          # Conectar a la base de datos
          conn = connect_db()
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
          self.ui.pushButton_Modificar_Empleado.show()
#---------------------------------------Consulta de INSUMOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def mostrar_insumos(self):
      try:
          # Conectar a la base de datos
          conn = connect_db()
          cursor = conn.cursor()

          # Obtener todos los insumos
          cursor.execute("SELECT * FROM Insumo")
          insumos = cursor.fetchall()

          # Mostrar los insumos en la tabla
          self.ui.tabla_Consultar_Insumo.clearContents()
          self.ui.tabla_Consultar_Insumo.setRowCount(len(insumos))
          headers = ["ID","NOMBRE","EXISTENCIA","DESCRIPCION"]
          self.ui.tabla_Consultar_Insumo.setColumnCount(len(headers))
          self.ui.tabla_Consultar_Insumo.setHorizontalHeaderLabels(headers)
          self.ui.tabla_Consultar_Insumo.verticalHeader().setVisible(False)
          # Ajustar el tamaño de los encabezados al contenido
          header = self.ui.tabla_Consultar_Insumo.horizontalHeader()
          header.setSectionResizeMode(QHeaderView.ResizeToContents)
          for i, insumo in enumerate(insumos):
              for j, valor in enumerate(insumo):
                  item = QTableWidgetItem(str(valor))
                  item.setTextAlignment(Qt.AlignCenter)  # Centrar el texto en la celda
                  self.ui.tabla_Consultar_Insumo.setItem(i, j, item)
                      # Ajustar el ancho de las columnas al contenido


      except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al mostrar los insumos: {str(e)}")
      finally:
          # Cerrar la conexión a la base de datos
          conn.close()
#---------------------------------------Modificar INSUMOS en la BASE DE DATOS-----------------------------------------------------
  @Slot()
  def modificar_buscar_inusmo(self):
    try:
      id_insumo = self.ui.lineEdit_Buscar_Insumo_5.text()
      insumo = buscar_insumo(self, id_insumo)
      if insumo:
          self.ui.ID_Modificar_Insumo.setText(str(insumo[0]))
          self.ui.lineEdit_Nombre_Insumo_2.setText(str(insumo[1]))
          self.ui.SpinBox_Existencia_2.setValue(int(insumo[2]))
          self.ui.textEdit_Descripcion_2.setText(str(insumo[3]))
      else:
          # Manejar el caso en que no se encuentre el insumo
         QMessageBox.warning(self, "Insumo no encontrado", "No se encontró un insumo con el ID especificado.")
    except sqlite3.Error as e:
      # Mostrar un mensaje de error si hay un problema con la base de datos
      print(id_insumo)  # Para verificar el valor de id_insumo
      QMessageBox.critical(self, "Error", f"Error al buscar el insumo con ID {id_insumo} en la base de datos: {str(e)}")
    finally :
       self.ui.pushButton_Modificar_Inusmo.show()
  @Slot()
  def modificar_inusmo(self):
      # Mostrar un mensaje de confirmación
      respuesta = QMessageBox.question(self, "Confirmar registro", "¿Desea modificar el insumo?",
                                        QMessageBox.Yes | QMessageBox.No)
      
      if respuesta == QMessageBox.Yes:
        try:
          # Conectar a la base de datos
          conn = connect_db()
          cursor = conn.cursor()

          # Obtener los valores de los campos de entrada
          id_insumo = self.ui.ID_Modificar_Insumo.text()
          nombre = self.ui.lineEdit_Nombre_Insumo_2.text()
          existencia = self.ui.SpinBox_Existencia_2.value()
          descripcion = self.ui.textEdit_Descripcion_2.toPlainText()

          # Modificar los valores en la tabla Insumo
          cursor.execute("UPDATE Insumo SET nombre=?, existencia=?, descripcion=? WHERE id=?", 
                        (nombre, existencia, descripcion, id_insumo))

          if cursor.rowcount > 0:
            # Confirmar la modificación
            conn.commit()
            # Mostrar un mensaje de éxito
            QMessageBox.information(self, "Modificación exitosa", "El insumo se ha modificado correctamente.")
          else:
              # Mostrar un mensaje de error si no se encontró el ID del proveedor
              QMessageBox.critical(self, "Error", "ID de insumo no encontrado.")
        except sqlite3.Error as e:
          # Mostrar un mensaje de error si ocurre un problema
          QMessageBox.critical(self, "Error", f"Error al registrar el empleado: {str(e)}")
        finally:
          # Cerrar la conexión a la base de datos
          conn.close()
          # Limpiar informacion capturada
          self.ui.lineEdit_Buscar_Insumo_5.clear()
          self.ui.ID_Modificar_Insumo.setText("-")
          self.ui.lineEdit_Nombre_Insumo_2.clear()
          self.ui.SpinBox_Existencia_2.clear()
          self.ui.textEdit_Descripcion_2.clear()    
  #(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((NAVEGACION)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
  @Slot()
  def navegar_inicio(self):
    self.stackedWidget.setCurrentIndex(0)
  @Slot()
  def navegar_comandas(self):
    self.stackedWidget.setCurrentIndex(1)
    self.ui.tab_Comandas.setCurrentIndex(0)
    self.ui.pushButton_Agregar_Platillos_Comanda.hide()

    next_id = get_cont_comanda(self)
    next_id += 1
    self.ui.ID_Comanda.setText(str(next_id))
    fecha = datetime.now().date()
    fecha_actual = fecha.strftime("%d-%m-%Y")
    self.ui.fecha_comanda.setText(str(fecha_actual))
    index = self.ui.tab_Comandas.indexOf(self.ui.ConsultarComanda)
    self.ui.tab_Comandas.removeTab(index)


  @Slot()
  def navegar_platillos(self):
    self.stackedWidget.setCurrentIndex(2)
    self.ui.tab_Platillos.setCurrentIndex(0)
    self.ui.pushButton_Agregar_Insumo.hide()

    next_id = get_cont_platillos(self)
    next_id += 1
    self.ui.ID_Platillo.setText(str(next_id))
    #self.ui.pushButton_Modificar_Inusmo.hide()
  @Slot()
  def navegar_compras(self):
    self.stackedWidget.setCurrentIndex(3)
    self.ui.tab_Compras.setCurrentIndex(0)

    index_consulta = self.ui.tab_Compras.indexOf(self.ui.ConsultarCompra)
    self.ui.tab_Compras.removeTab(index_consulta)
    index_mod = self.ui.tab_Compras.indexOf(self.ui.ModificarCompra)
    self.ui.tab_Compras.removeTab(index_mod)
  @Slot()
  def navegar_insumos(self):
    self.stackedWidget.setCurrentIndex(4)
    self.ui.tab_Insumo.setCurrentIndex(0) 

    next_id = get_cont_insumo(self)
    next_id += 1
    self.ui.ID_Insumo.setText(str(next_id))
    self.ui.pushButton_Modificar_Inusmo.hide()
  @Slot()
  def navegar_empleados(self):
    self.stackedWidget.setCurrentIndex(5)
    self.ui.tab_Empleados.setCurrentIndex(0)

    next_id = get_cont_empleado(self)
    next_id += 1
    self.ui.ID_Empleado.setText(str(next_id))
    self.ui.pushButton_Modificar_Empleado.hide()
  @Slot()
  def navegar_provedores(self):
    self.stackedWidget.setCurrentIndex(6)
    self.ui.tab_Proveedores.setCurrentIndex(0)

    next_id = get_cont_proveedor(self)
    next_id += 1
    self.ui.ID_Proveedor.setText(str(next_id))
    self.ui.pushButton_Modificar_Proveedor.hide()