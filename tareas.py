import json
import os
from datetime import datetime
from colorama import Fore, Style

ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, "r") as archivo:
                contenido = archivo.read().strip()
                if not contenido:
                    return []
                return json.loads(contenido)
        except json.JSONDecodeError:
            print(Fore.RED + "⚠️ El archivo de tareas está corrupto o vacío. Se iniciará una lista nueva." + Style.RESET_ALL)
            return []
    else:
        return []

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as archivo:
        json.dump(tareas, archivo, indent=4)

def agregar_tarea(descripcion):
    tareas = cargar_tareas()
    if any(t["descripcion"] == descripcion for t in tareas):
        print(Fore.RED + "⚠️ Esa tarea ya existe." + Style.RESET_ALL)
        return
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False,
        "fecha": datetime.now().isoformat()
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(Fore.GREEN + f"Tarea agregada: {descripcion}" + Style.RESET_ALL)

def listar_tareas(solo_completadas=False, solo_pendientes=False, solo_hoy=False, orden_descendente=True):
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas guardadas.")
        return

    if solo_completadas:
        tareas = [t for t in tareas if t["completada"]]

    if solo_pendientes:
        tareas = [t for t in tareas if not t["completada"]]

    if solo_hoy:
        hoy = datetime.now().date()
        tareas = [
            t for t in tareas
            if "fecha" in t and datetime.fromisoformat(t["fecha"]).date() == hoy
        ]

    tareas.sort(key=lambda t: t.get("fecha", ""), reverse=orden_descendente)

    print(Fore.YELLOW + "\n📋 Lista de tareas:" + Style.RESET_ALL)
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea["completada"] else "🔲"
        fecha_iso = tarea.get("fecha")
        if fecha_iso:
            try:
                fecha_obj = datetime.fromisoformat(fecha_iso)
                fecha_legible = fecha_obj.strftime("%d/%m/%Y %H:%M")
            except ValueError:
                fecha_legible = "fecha inválida"
        else:
            fecha_legible = "sin fecha"

        print(f"{i}. {estado} {tarea['descripcion']} ({fecha_legible})")

def completar_tarea(numero):
    tareas = cargar_tareas()
    try:
        indice = int(numero) - 1
        if 0 <= indice < len(tareas):
            if tareas[indice]["completada"]:
                print(Fore.YELLOW + "⚠️ La tarea ya está completada." + Style.RESET_ALL)
                return
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print(Fore.GREEN + f"Tarea completada: {tareas[indice]['descripcion']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "⚠️ Número de tarea inválido." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "⚠️ Por favor, ingresá un número válido." + Style.RESET_ALL)

def desmarcar_tarea(numero):
    tareas = cargar_tareas()
    try:
        indice = int(numero) - 1
        if 0 <= indice < len(tareas):
            if not tareas[indice]["completada"]:
                print(Fore.YELLOW + "⚠️ La tarea ya está pendiente." + Style.RESET_ALL)
                return
            tareas[indice]["completada"] = False
            guardar_tareas(tareas)
            print(Fore.GREEN + f"Tarea desmarcada: {tareas[indice]['descripcion']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "⚠️ Número de tarea inválido." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "⚠️ Por favor, ingresá un número válido." + Style.RESET_ALL)

def eliminar_tarea(numero):
    tareas = cargar_tareas()
    try:
        indice = int(numero) - 1
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            guardar_tareas(tareas)
            print(Fore.GREEN + f"Tarea eliminada: {tarea_eliminada['descripcion']}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "⚠️ Número de tarea inválido." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "⚠️ Por favor, ingresá un número válido." + Style.RESET_ALL)
        
__all__ = [
    "cargar_tareas",
    "guardar_tareas",
    "agregar_tarea",
    "listar_tareas",
    "completar_tarea",
    "eliminar_tarea"
    "desmarcar_tarea"
]