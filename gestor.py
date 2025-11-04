import argparse

from tareas import (
    agregar_tarea,
    desmarcar_tarea,
    listar_tareas,
    completar_tarea,
    eliminar_tarea
)

def main():
    print("Bienvenido al gestor de tareas CLI")

    parser = argparse.ArgumentParser(description="Gestor de tareas CLI")
    parser.add_argument("comando", choices=["agregar", "listar", "completar", "eliminar", "desmarcar"], help="Comando a ejecutar")
    parser.add_argument("descripcion", nargs="?", help="Descripción o número de tarea")
    parser.add_argument("--completadas", action="store_true", help="Mostrar solo tareas completadas")
    parser.add_argument("--pendientes", action="store_true", help="Mostrar solo tareas pendientes")
    parser.add_argument("--hoy", action="store_true", help="Mostrar solo tareas creadas hoy")
    parser.add_argument("--ascendente", action="store_true", help="Ordenar por fecha ascendente")


    args = parser.parse_args()

    if args.comando == "agregar":
        if args.descripcion:
            agregar_tarea(args.descripcion)
        else:
            print("Por favor, proporcioná una descripción para la tarea.")

    elif args.comando == "listar":
        listar_tareas(
            solo_completadas=args.completadas,
            solo_pendientes=args.pendientes,
            solo_hoy=args.hoy,
            orden_descendente=not args.ascendente
        )

    elif args.comando == "completar":
        if args.descripcion:
            completar_tarea(args.descripcion)
        else:
            print("Por favor, proporcioná el número de la tarea a completar.")

    elif args.comando == "eliminar":
        if args.descripcion:
            eliminar_tarea(args.descripcion)
        else:
            print("Por favor, proporcioná el número de la tarea a eliminar.")
            
    elif args.comando == "desmarcar":
        if args.descripcion:
            desmarcar_tarea(args.descripcion)
        else:
            print("Por favor, proporcioná el número de la tarea a desmarcar.")

if __name__ == "__main__":
    main()
