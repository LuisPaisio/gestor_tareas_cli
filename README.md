# 🧠 Gestor de Tareas CLI

Un gestor de tareas simple y modular hecho en Python, ejecutable desde la terminal. Permite agregar, listar, completar y eliminar tareas, con persistencia en formato JSON.

## 🚀 Características

- Agregar tareas con descripción
- Listar tareas con estado (completada o pendiente)
- Marcar tareas como completadas
- Eliminar tareas por número
- Persistencia en `tareas.json`
- Colores en terminal con `colorama`
- Estructura modular para escalar fácilmente

## 📁 Estructura del proyecto

gestor_tareas_cli/ 
├── gestor.py # Punto de entrada principal 
├── tareas.py # Funciones de lógica de tareas 
├── helpers.py # Funciones auxiliares (opcional) 
├── tareas.json # Archivo de datos 
├── requirements.txt # Dependencias del proyecto

## 🛠️ Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/tuusuario/gestor_tareas_cli.git
cd gestor_tareas_cli
```

2. Creá y activá un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

## 🧪 Uso

1. Agregar una tarea:

```bash
python gestor.py agregar "Estudiar Python"
```

2. Listar tareas:
```bash
python gestor.py listar
```

3. Filtrar tareas:
```bash
python gestor.py listar --completadas
python gestor.py listar --pendientes
python gestor.py listar --hoy
python gestor.py listar --ascendentes
```

4. Marcar como completada:
```bash
python gestor.py completar 1
```

5. Eliminar una tarea:
```bash
python gestor.py eliminar 2
```

## 📦 Requisitos

- Python 3.10+
- Colorama

## ▶️ Ejecutar los tests

- Desde la raíz del proyecto:
```bash
python -m tests.test_tareas
```

## 🧠 ¿Qué se prueba?

- Agregar tareas sin duplicados
- Completar tareas por número
- Eliminar tareas correctamente
- Validaciones de entrada
- Filtros por estado y fecha

## 📌 Autor

- Luis — [Linkedin](www.linkedin.com/in/luis-paisio)
- Proyecto desarrollado como parte de su portfolio técnico.

