import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tareas import agregar_tarea, cargar_tareas, guardar_tareas

import unittest
from tareas import agregar_tarea, cargar_tareas, guardar_tareas

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        # Crear una lista de tareas vacía para pruebas
        self.tareas = []

    def test_agregar_tarea(self):
        descripcion = "Probar test"
        agregar_tarea(descripcion)
        tareas = cargar_tareas()
        self.assertTrue(any(t["descripcion"] == descripcion for t in tareas))

if __name__ == "__main__":
    unittest.main()
