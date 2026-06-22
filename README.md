# 🚀 PROYECTO DE AUTOMATIZACIÓN QA - KARINA REGUERA

## 📌 Descripción
Proyecto de automatización de pruebas funcionales realizado con **Python**, **Selenium WebDriver**, **Pytest** y **GitHub Actions (CI/CD)**.  
El objetivo es validar el correcto funcionamiento de una aplicación web mediante pruebas automatizadas, generando evidencia y reportes en formato **HTML**.

---

## 🛠️ Tecnologías usadas
- 🐍 Python  
- 🌐 Selenium + WebDriver-Manager  
- 🧪 Pytest  
- 📊 Pytest-HTML (reportes)  
- ✅ Pytest-Check  
- 🔗 Requests  
- 📖 Behave (BDD)  
- 💻 Git & GitHub  
- ⚙️ GitHub Actions (CI/CD)

---

## 🚀 Instalación
Clonar el repositorio:

```bash
git clone https://github.com/KarinaReguera/PROYECTO-QA-KARINA-REGUERA.git


## Instalación de dependencias
pip install -r requirements.txt


## Ejecución de pruebas en consola Python
pytest --html=report.html --self-contained-html

## Funcionamiento de las pruebas:
- Test Login → Verifica acceso correcto con credenciales válidas.
- Test Inventario → Valida que los productos se muestren correctamente.
- Test Cart → Comprueba la funcionalidad del carrito de compras.

## 📂 Estructura del proyecto
```
📁 PROYECTO-QA-KARINA-REGUERA/
│
├── .github/
│   └── workflows/
│       └── tests.yml                # Workflow de GitHub Actions
├── data/                            # Datos de prueba
│   ├── products.json
│   └── users.csv
│
├── features/                        # Escenarios BDD (Behave/Cucumber)
│   ├── steps/
│   │   ├── login_steps.py
│   │   └── environment.py
│   └── login.feature
│
├── logs/                            # Logs de ejecución
│   └── test_log_22062026.log
│
├── page/                            # Page Objects (Selenium)
│   ├── cart_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/
│   └── screenshots/
│       └── test_login_invalid_password.png
│
├── test/                            # Casos de prueba automatizados
│   ├── test_api_metodos.py
│   ├── test_api.py
│   ├── test_cart_json.py
│   ├── test_cart.py
│   ├── test_inventory.py
│   ├── test_login_csv.py
│   └── test_login.py
│
├── utils/                           # Utilidades y helpers
│   ├── data_reader.py
│   ├── logger.py
│
├── conftest.py                      # Configuración global de Pytest
├── pytest.ini                       # Parámetros de ejecución
├── report.html                      # Reporte HTML generado por Pytest
├── requirements.txt                 # Dependencias del proyecto
├── selectors.md                     # Referencia de selectores para Selenium
└── README.md                        # Documentación principal

## ⚙️ Flujo de ejecución
- Pytest ejecuta los casos de prueba definidos en test/.
- Los Page Objects en page/ encapsulan la lógica de interacción con la UI.
- Los datos se cargan desde data/ mediante utils/data_reader.py.
- Los resultados y capturas se guardan en reports/.
- El workflow tests.yml en .github/workflows/ ejecuta todo automáticamente en GitHub Actions.


## 📊 Reportes
Los resultados se generan en formato HTML dentro del archivo report.html


## 🌐 Repositorio GitHub

🔗 PROYECTO-QA-KARINA-REGUERA

