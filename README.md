# 🧠 Gestor de Tareas CLI + Web

Aplicación para gestionar tareas desde la terminal o desde una interfaz web. Permite agregar, listar, completar, desmarcar y eliminar tareas, con filtros por estado, fecha y orden. Desarrollado en Python con Flask.

## 🚀 Características

- Agregar tareas con descripción
- Listar tareas con estado (completada o pendiente)
- Marcar tareas como completadas
- Eliminar tareas por número
- Filtros: completadas, pendientes, hoy, orden ascendente/descendente
- Interfaz web con Flask
- Estilos personalizados con CSS
- Persistencia en `tareas.json`
- Colores en terminal con `colorama`
- Estructura modular para escalar fácilmente

## 📁 Estructura del proyecto

```bash
gestor_tareas_cli/ 
├── gestor.py # Punto de entrada principal 
├── tareas.py # Funciones de lógica de tareas 
├── helpers.py # Funciones auxiliares (opcional) 
├── tareas.json # Archivo de datos 
├── requirements.txt # Dependencias del proyecto
```

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
python tareas.py agregar "Estudiar Python"
```

2. Listar tareas:
```bash
python tareas.py listar
```

3. Filtrar tareas:
```bash
python tareas.py listar --completadas
python tareas.py listar --pendientes
python tareas.py listar --hoy
python tareas.py listar --ascendentes
```

4. Marcar como completada:
```bash
python tareas.py completar 1
```

4. Desmarcar:
```bash
python tareas.py desmarcar 1
```

5. Eliminar una tarea:
```bash
python tareas.py eliminar 2
```

## 🌐 Uso Web
```bash
python app.py
```

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

## 📦 Requisitos

- Python 3.10+
- Colorama

## 📌 Autor

- Luis — [Linkedin](www.linkedin.com/in/luis-paisio)
- Proyecto desarrollado como parte de su portfolio técnico.

