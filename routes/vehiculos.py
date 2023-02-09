from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.vehiculos import Vehiculo
from utils.db import db

vehiculos = Blueprint("vehiculos", __name__)


@vehiculos.route("/")
def index(): 
    vehiculos = Vehiculo.query.all()
    return render_template("index.html", vehiculos = vehiculos)


@vehiculos.route("/new", methods=["POST"])
def add_vehiculo():
    patente = request.form["patente"]
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    anio = request.form["anio"]
    kilometraje = request.form["kilometraje"]
    combustible = request.form["combustible"]

    new_vehiculo = Vehiculo(patente, marca, modelo, anio, kilometraje, combustible)
    
    db.session.add(new_vehiculo)
    db.session.commit()

    flash('El nuevo vehiculo se ha registrado exitosamente.')

    return redirect(url_for('vehiculos.index'))


@vehiculos.route("/update/<id>", methods = ['POST','GET'])
def update_vehiculo(id):
    vehiculo = Vehiculo.query.get(id)

    if request.method == 'POST':
        vehiculo.patente = request.form["patente"]
        vehiculo.marca = request.form["marca"]
        vehiculo.modelo = request.form["modelo"]
        vehiculo.anio = request.form["anio"]
        vehiculo.kilometraje = request.form["kilometraje"]
        vehiculo.combustible = request.form["combustible"]
        
        db.session.commit()

        flash('El vehiculo ha sido actualizado.')
        return redirect(url_for('vehiculos.index'))
    
    return render_template('update.html', vehiculo=vehiculo)


@vehiculos.route("/delete/<id>")
def delete_vehiculo(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()

    flash('Vehiculo borrado exitosamente.')
    return redirect(url_for('vehiculos.index'))