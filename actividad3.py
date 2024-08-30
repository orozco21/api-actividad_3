from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
HOST = 	'127.0.0.1'
USER = 'root'
PASSWORD = ''
DB = 'mi_tienda'

# Conexión a la base de datos
conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB)

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    return jsonify(usuarios)

# Obtener un usuario por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = %s', (id,))
    usuario = cursor.fetchone()
    return jsonify(usuario)

# Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, email) VALUES (%s, %s)', (data['nombre'], data['email']))
    conn.commit()
    return jsonify({'mensaje': 'Usuario creado con éxito'})

# Actualizar un usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s', (data['nombre'], data['email'], id))
    conn.commit()
    return jsonify({'mensaje': 'Usuario actualizado con éxito'})

# Eliminar un usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (id,))
    conn.commit()
    return jsonify({'mensaje': 'Usuario eliminado con éxito'})

# Obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    return jsonify(productos)

# Obtener un producto por ID
@app.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = %s', (id,))
    producto = cursor.fetchone()
    return jsonify(producto)

# Crear un nuevo producto
@app.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio) VALUES (%s, %s)', (data['nombre'], data['precio']))
    conn.commit()
    return jsonify({'mensaje': 'Producto creado con éxito'})

# Actualizar un producto
@app.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('UPDATE productos SET nombre = %s, precio = %s WHERE id = %s', (data['nombre'], data['precio'], id))
    conn.commit()
    return jsonify({'mensaje': 'Producto actualizado con éxito'})

# Eliminar un producto
@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = %s', (id,))
    conn.commit()
    return jsonify({'mensaje': 'Producto eliminado con éxito'})

if __name__ == '__main__':
    app.run(debug=True)