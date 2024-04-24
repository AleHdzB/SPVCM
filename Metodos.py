import sqlite3

def get_cont_insumo(self):
    conn = sqlite3.connect("C:\\Users\\Ale\\Documents\\GitHub\\SPVCM\\DataBase.db")
    cursor = conn.cursor()

    # Ejecuta la consulta para obtener el ID máximo
    cursor.execute("SELECT MAX(id) FROM Insumo")
    max_id = cursor.fetchone()[0]  # Obtiene el valor del ID máximo
    # Cierra la conexión a la base de datos
    return max_id

def buscar_insumo(self,id_insumo):
    # Conectar a la base de datos
    conn = sqlite3.connect("C:\\Users\\Ale\\Documents\\GitHub\\SPVCM\\DataBase.db")
    cursor = conn.cursor()

    # Consulta para obtener los datos del insumo por su ID
    cursor.execute("SELECT * FROM Insumo WHERE id = ?", (id_insumo,))
    insumo = cursor.fetchone()  # Obtener el primer resultado
    return insumo