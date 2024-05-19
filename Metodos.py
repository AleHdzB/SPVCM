import sqlite3
import os
# Construir la ruta relativa de la base de datos
db_path = os.path.join(os.path.dirname(__file__), 'DataBase.db')

def connect_db():
    return sqlite3.connect(db_path)

# Uso del cursor y la conexión como antes

def get_cont_insumo(self):
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Ejecuta la consulta para obtener el ID máximo
    cursor.execute("SELECT MAX(id) FROM Insumo")
    max_id = cursor.fetchone()[0]  # Obtiene el valor del ID máximo
    if max_id is None:
        max_id = 0
    return max_id

def buscar_insumo(self,id_insumo):
    # Conectar a la base de datos
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Consulta para obtener los datos del insumo por su ID
    cursor.execute("SELECT * FROM Insumo WHERE id = ?", (id_insumo,))
    insumo = cursor.fetchone()  # Obtener el primer resultado
    return insumo
def buscar_empleado(self,id_empleado):
    # Conectar a la base de datos
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Consulta para obtener los datos del insumo por su ID
    cursor.execute("SELECT * FROM Empleado WHERE id = ?", (id_empleado,))
    empleado = cursor.fetchone()  # Obtener el primer resultado
    return empleado

def buscar_proveedor(self,id_proveedor):
    # Conectar a la base de datos
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Consulta para obtener los datos del insumo por su ID
    cursor.execute("SELECT * FROM Proveedor WHERE id = ?", (id_proveedor,))
    proveedor = cursor.fetchone()  # Obtener el primer resultado
    return proveedor

def get_cont_empleado(self):
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Ejecuta la consulta para obtener el ID máximo
    cursor.execute("SELECT MAX(id) FROM Empleado")
    max_id = cursor.fetchone()[0]  # Obtiene el valor del ID máximo
    if max_id is None:
        max_id = 0
    return max_id


def get_cont_proveedor(self):
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Ejecuta la consulta para obtener el ID máximo
    cursor.execute("SELECT MAX(id) FROM Proveedor")
    max_id = cursor.fetchone()[0]  # Obtiene el valor del ID máximo
    if max_id is None:
        max_id = 0
    return max_id

def get_cont_platillos(self):
    conn = conn = connect_db()
    cursor = conn.cursor()

    # Ejecuta la consulta para obtener el ID máximo
    cursor.execute("SELECT MAX(id) FROM Platillo")
    max_id = cursor.fetchone()[0]  # Obtiene el valor del ID máximo
    if max_id is None:
        max_id = 0
    return max_id

def itemToString(item):
    return item.text()

def itemToFloat(item):
    text = item.text()
    real = float(text)
    return real
def itemToInt(item):
    text = item.text()
    entero = int(text)
    return entero