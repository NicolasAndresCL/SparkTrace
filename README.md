# ⚡ SparkTrace — Backend Audit & Dashboard

🇪🇸 SparkTrace es un backend modular para carga masiva, sincronización entre sistemas y trazabilidad reproducible. Usa Django REST Framework, comandos desacoplados, testing automatizado y documentación bilingüe. Diseñado para integrarse con proyectos como Tiendita de Marian, con enfoque en auditoría, compatibilidad internacional y presentación técnica.

🇬🇧 SparkTrace is a modular backend for bulk loading, cross-system sync, and reproducible traceability. Built with Django REST Framework, decoupled commands, automated testing, and bilingual documentation. Designed to integrate with projects like Tiendita de Marian, with focus on auditing, international compatibility, and technical presentation.
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
│     ├── dashboard/ # Visualización técnica 
│     ├── spark_jobs/ # Jobs PySpark 
│     ├── core/ # Configuración y utilidades 
│     ├── management/commands/ # Comandos para lanzar jobs 
│     ├── settings.py 
│     ├── settings_test.py # Configuración desacoplada para CI 
│     └── urls.py 
├── productos/
│     ├───migrations
│     ├───services
│     ├───tests
│     ├───utils
│     └───integraciones
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

## 🧪 API Integration Testing / Pruebas de Integración con API

This module validates the integration with Tiendita API using real fixtures and simulated responses.

Este módulo valida la integración con la API de Tiendita utilizando fixtures reales y respuestas simuladas.

- ✅ Valid products / Productos válidos
- ❌ Missing fields / Campos faltantes
- ⚠️ Unexpected responses / Respuestas inesperadas
- 🧾 Custom exception: `APIError` / Excepción personalizada: `APIError`

All tests are reproducible and designed for international portfolio presentation.

Todas las pruebas son reproducibles y están diseñadas para presentación en portafolios internacionales.

---
## 🧮 Technical Audit / Auditoría Técnica

All modules are validated through automated tests with real fixtures, simulated errors, and command execution.

Todos los módulos están validados mediante pruebas automatizadas con fixtures reales, errores simulados y ejecución de comandos.

| Area / Área                  | Validation / Validación |
|-----------------------------|--------------------------|
| API Integration / Integración API | ✅ Real fixtures, error handling |
| CSV Loader / Cargador CSV         | ✅ Valid and invalid data |
| Spark Jobs / Comandos Spark       | ✅ Execution and registration |
| Exception Handling / Manejo de excepciones | ✅ Custom `APIError` |


## 📊 Coverage Report / Informe de Cobertura

This project maintains a high level of test coverage to ensure reliability and reproducibility.

Este proyecto mantiene un alto nivel de cobertura de pruebas para garantizar confiabilidad y reproducibilidad.

| Module / Módulo              | Coverage / Cobertura | Status / Estado |
|-----------------------------|----------------------|------------------|
| `test_tiendita_api.py`      | 100 %                | ✅ Complete / Completo |
| `test_csv_loader.py`        | 100 %                | ✅ Complete / Completo |
| `tiendita.py`               | 83 %                 | ⚠️ Partial / Parcial |
| `csv_loader.py`             | 79 %                 | ⚠️ Partial / Parcial |
| Global coverage / Cobertura global | 94 %         | 🚀 High / Alta |

All tests are designed to validate real scenarios, simulate edge cases, and ensure traceable behavior across modules.

Todas las pruebas están diseñadas para validar escenarios reales, simular casos límite y asegurar comportamiento trazable entre módulos.


## 👨‍💻 Autor / Author
Nicolás Andrés Cano Leal Backend Developer especializado en Django, FastAPI, auditoría y CI/CD. Backend Developer focused on Django, FastAPI, auditing and CI/CD.

🌐 Portafolio: nicolasandrescl.pythonanywhere.com

💼 LinkedIn: linkedin.com/in/nicolas-andres-cano-leal

## 📜 Licencia / License
Este proyecto está bajo la licencia MIT. This project is licensed under the MIT License.