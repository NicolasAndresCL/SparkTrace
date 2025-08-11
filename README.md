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
├── config/              # Settings desacoplados (base, dev, prod, test)
├── core/                # Auditoría, productos, carga masiva
├── dashboard/           # Dash + PySpark
├── tests/               # Tests unitarios y mocks
├── media/               # Archivos multimedia
├── staticfiles/         # Archivos estáticos
└── README.md
```

---

## 👨‍💻 Autor / Author
Nicolás Andrés Cano Leal Backend Developer especializado en Django, FastAPI, auditoría y CI/CD. Backend Developer focused on Django, FastAPI, auditing and CI/CD.

🌐 Portafolio: nicolasandrescl.pythonanywhere.com

💼 LinkedIn: linkedin.com/in/nicolas-andres-cano-leal

## 📜 Licencia / License
Este proyecto está bajo la licencia MIT. This project is licensed under the MIT License.