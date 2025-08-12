# ⚡ SparkTrace — Backend Audit & Dashboard

Backend modular en Django + FastAPI para trazabilidad de eventos, carga masiva de productos con imágenes, y visualización técnica vía Dash. Diseñado para entrevistas internacionales y despliegue multiplataforma.

Modular Django + FastAPI backend for event auditing, bulk product upload with images, and technical dashboard via Dash. Built for international interviews and multiplatform deployment.

---

## 🧠 Características / Features

- 🕵️ Auditoría automática de eventos con señales y JSONField seguro  
  Automatic event audit via Django signals and secure JSONField

- 🧪 Testing desacoplado con SQLite en memoria y backend de correo local  
  Decoupled testing with in-memory SQLite and local email backend

- 🚀 CI/CD con cobertura total y migraciones automatizadas  
  Full coverage CI/CD with automated migrations and cleanup

- 📦 Carga masiva de productos con imágenes desde CSV  
  Bulk product upload with image validation and safe file association

- 📊 Dashboard técnico con PySpark + Dash para visualización  
  Technical dashboard via PySpark + Dash for data insights

- 🌐 Documentación bilingüe y override visual de Swagger UI  
  Bilingual documentation and professional Swagger UI override

---

## 🧪 Testing & CI/CD

```bash
# Ejecutar tests con settings desacoplado
pytest --ds=config.settings_test

# Generar cobertura y badge para README
coverage run -m pytest --ds=config.settings_test
coverage report
coverage-badge -o coverage.svg
```

---

## 📁 Estructura del proyecto / Project Structure
```
 
sparktrace/ 
├── config/ 
│     ├── auditlog/ # Auditoría de eventos 
│     ├── products/ # Carga masiva y validación 
│     ├── dashboard/ # Visualización técnica 
│     ├── spark_jobs/ # Jobs PySpark 
│     ├── core/ # Configuración y utilidades 
│     ├── management/commands/ # Comandos para lanzar jobs 
│     ├── settings.py 
│     ├── settings_test.py # Configuración desacoplada para CI 
│     └── urls.py 
├── sparktrace_dashboard/ # Dash o Plotly para visualización 
├── tests/ 
│     ├── mocks/ # Mock de SparkSession 
│     └── test_jobs.py 
├── requirements.txt 
├── manage.py 
├── env
├── .gitgnore 
├── .env
├── .env.test
├── .env.main
├── .env.dev
└── README.md 
```


---


## 🪝 Git Hooks versionados / Versioned Git Hooks

Este proyecto utiliza hooks personalizados en `.githooks/` para automatizar tareas según la rama activa.  
This project uses custom hooks in `.githooks/` to automate tasks based on the active branch.

## 🔄 Cambio automático de entorno / Automatic environment switching

Al cambiar de rama, el hook `post-checkout` selecciona el archivo `.env` correspondiente:

| Rama / Branch | Archivo `.env` usado / Selected `.env` |
|---------------|----------------------------------------|
| `test`        | `.env.test`                            |
| `dev`         | `.env.dev`                             |
| `main`        | `.env.main`                            |

## ⚙️ Activación del sistema de hooks / Hook system activation

```bash
git config core.hooksPath .githooks
chmod +x .githooks/post-checkout
```
Esto asegura que el entorno se configure automáticamente al cambiar de rama, evitando errores humanos y mejorando la trazabilidad en CI/CD. 
This ensures automatic environment setup when switching branches, reducing human error and improving CI/CD traceability.
---

## ⚙️ Comandos de gestión / Management Commands

Estos comandos automatizan la carga de productos, la integración externa y el monitoreo técnico.  
These commands automate product loading, external sync, and technical monitoring.

---

### 1. `cargar_productos.py`

📦 Carga productos desde un archivo CSV a la base de datos local.  
📦 Loads products from a CSV file into the local database.

```bash
python manage.py cargar_productos --csv=data/productos.csv
```
-✅ Valida campos e imágenes / Validates fields and image paths

-🔁 Activa eventos de auditoría / Triggers audit events

-🧪 Útil para testing y setup local / Useful for testing and local setup

---

## 2. subir_a_tiendita.py
🌐 Envía productos desde un CSV a la API externa de Tiendita. 🌐 Sends products from a CSV file to the external Tiendita API.

```bash
python manage.py subir_a_tiendita --csv=data/productos.csv
```
- ✅ Valida campos e imágenes / Validates fields and image paths

- 🔁 Activa eventos de auditoría / Triggers audit events

- 🧪 Útil para testing y setup local / Useful for testing and local setup

---

## 3. run_spark_job.py
📊 Ejecuta un job PySpark para análisis técnico y generación de dashboard. 📊 Executes a PySpark job for technical analysis and dashboard generation.

```bash   
python manage.py run_spark_job
```
- ⚙️ Procesa datos en paralelo / Processes product data in parallel

- 📈 Genera métricas y logs / Generates metrics and logs

- 📡 Alimenta el dashboard técnico / Feeds the technical dashboard

## 👨‍💻 Autor / Author
Nicolás Andrés Cano Leal Backend Developer especializado en Django, FastAPI, auditoría y CI/CD. Backend Developer focused on Django, FastAPI, auditing and CI/CD.

🌐 Portafolio: nicolasandrescl.pythonanywhere.com

💼 LinkedIn: linkedin.com/in/nicolas-andres-cano-leal

## 📜 Licencia / License
Este proyecto está bajo la licencia MIT. This project is licensed under the MIT License.