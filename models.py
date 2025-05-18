# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Modelo de empleado
class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)  # En un sistema real, usa hashing

# Modelo de registros de entrada/salida
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    fecha = db.Column(db.Date, default=datetime.today)
    hora = db.Column(db.Time, default=datetime.now().time)
    tipo = db.Column(db.String(10), nullable=False)  # "entrada" o "salida"

