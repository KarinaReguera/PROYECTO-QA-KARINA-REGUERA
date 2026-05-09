# PROYECTO DE AUTOMATIZACIÓN QA - KARINA REGUERA

## 📌 Descripción
Proyecto de automatización de pruebas funcionales realizado con **Python**, **Selenium WebDriver** y **Pytest**.  
El objetivo es validar el correcto funcionamiento de una aplicación web mediante pruebas automatizadas, generando evidencia y reportes HTML.

## 🛠️ Tecnologías usadas
- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML (reportes)
- Git
- GitHub

## 🚀 Instalación
Clonar el repositorio:

git clone https://github.com/usuario/proyecto-qa.git

## Instalación de dependencias
pip install -r requirements.txt

## Ejecución de pruebas en consola Python
pytest --html=report.html --self-contained-html

## Funcionamiento de las pruebas:
- Test Login → Verifica acceso correcto con credenciales válidas.
- Test Inventario → Valida que los productos se muestren correctamente.
- Test Cart → Comprueba la funcionalidad del carrito de compras.


## 📂 Estructura del proyecto
PROYECTO-QA-KARINA-REGUERA/
│── tests/                 # Casos de prueba automatizados
│   ├── test_login.py      # Validación de login
│   ├── test_inventario.py # Validación de inventario
│   └── test_cart.py       # Validación de carrito de compras
│── utils/                 # Clases y funciones auxiliares
│   ├── LoginPage.py       # Instrucciones para el login
│── conftest.py            # Configuración y fixtures de Pytest
│── pytest.ini             # Parámetros de ejecución de Pytest
│── requirements.txt       # Dependencias del proyecto
│── README.md              # Documentación


📊 Reportes
Los resultados se generan en formato HTML dentro del archivo report.html.
