from utils.db import db

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    patente = db.Column(db.String(10))
    marca = db.Column(db.String(100) )
    modelo = db.Column(db.String(100))
    anio = db.Column(db.Integer)
    kilometraje = db.Column(db.Integer)
    combustible = db.Column(db.Integer)

    def __init__(self, patente, marca, modelo, anio, kilometraje, combustible):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.combustible = combustible