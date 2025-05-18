# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Empleado, Registro
from datetime import datetime, time
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretoseguro'
db.init_app(app)

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()
    # Crear empleado demo si no existe
with app.app_context():
    if not Empleado.query.filter_by(correo="demo@empresa.com").first():
        nuevo = Empleado(nombre="Empleado Demo", correo="demo@empresa.com", contrasena="1234")
        db.session.add(nuevo)
        db.session.commit()
        print("Empleado demo creado: demo@empresa.com / 1234")


@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Página de login
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        empleado = Empleado.query.filter_by(correo=correo, contrasena=contrasena).first()
        if empleado:
            session['empleado_id'] = empleado.id
            return redirect(url_for('dashboard'))
        else:
            return "Credenciales inválidas"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # Página de registro de asistencia
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        tipo = request.form['tipo']
        registro = Registro(
            empleado_id=session['empleado_id'],
            tipo=tipo,
            hora=datetime.now().time()
        )
        db.session.add(registro)
        db.session.commit()
        return f"{tipo.capitalize()} registrada correctamente a las {registro.hora}"

    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
