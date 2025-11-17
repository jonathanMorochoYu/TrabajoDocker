from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Microservicio de Usuarios funcionando!"

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conexion = mysql.connector.connect(
        host='db',
        user='root',
        password='12345',
        database='usuarios_db'
    )
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    conexion.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
