from flask import Flask, render_template, redirect, request
from tareas import (
    cargar_tareas,
    agregar_tarea,
    completar_tarea,
    desmarcar_tarea,
    eliminar_tarea
)
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    tareas = cargar_tareas()

    # Filtros desde query params
    solo_completadas = request.args.get("completadas") == "1"
    solo_pendientes = request.args.get("pendientes") == "1"
    solo_hoy = request.args.get("hoy") == "1"
    orden_descendente = request.args.get("ascendente") != "1"

    # Aplicar filtros
    if solo_completadas:
        tareas = [t for t in tareas if t["completada"]]
    if solo_pendientes:
        tareas = [t for t in tareas if not t["completada"]]
    if solo_hoy:
        hoy = datetime.now().date().isoformat()
        tareas = [t for t in tareas if t["fecha"].startswith(hoy)]
    tareas.sort(key=lambda t: t.get("fecha", ""), reverse=orden_descendente)

    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    descripcion = request.form.get("descripcion")
    if descripcion:
        agregar_tarea(descripcion)
    return redirect("/")

@app.route("/completar/<int:indice>")
def completar(indice):
    completar_tarea(str(indice))
    return redirect("/")

@app.route("/desmarcar/<int:indice>")
def desmarcar(indice):
    desmarcar_tarea(str(indice))
    return redirect("/")

@app.route("/eliminar/<int:indice>")
def eliminar(indice):
    eliminar_tarea(str(indice))
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

