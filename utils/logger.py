#  EL LOGGER REGISTRA TODOS LOS EVENTOS, ACCIONES Y MENSAJES DURANTE LA EJECUCION DE LOS TESTS.

# Este archivo contiene la configuración del logger para el proyecto de automatización de pruebas. Se importan los módulos necesarios para configurar el logger, como logging para registrar eventos, pathlib para manejar rutas de archivos y datetime para obtener la fecha y hora actual. Se crea una carpeta "logs" para almacenar los archivos de registro generados por el logger, y se configura el logger con un formato específico para los mensajes de registro. Finalmente, se crea una instancia del logger con un nombre específico que se utilizará en todo el proyecto para registrar eventos relevantes durante la ejecución de las pruebas.




import logging # Importo el módulo logging para poder utilizarlo en la función pytest_runtest_makereport para registrar información sobre los tests que se están ejecutando, como el nombre del test, el resultado del test, y cualquier mensaje de error o información adicional que se desee registrar.

import pathlib # Importo el módulo pathlib para poder utilizarlo en la función pytest_runtest_makereport para construir la ruta del archivo de captura de pantalla de manera más flexible y compatible con diferentes sistemas operativos.

from datetime import datetime # Importo la clase datetime del módulo datetime para poder utilizarla en la función pytest_runtest_makereport para obtener la fecha y hora actual al momento de tomar la captura de pantalla, lo que permite nombrar el archivo de captura de pantalla de manera única y organizada. FECHA Y HORA


logs_dir = pathlib.Path("logs") # Crea en la raíz el proyecto una carpeta llamada logs, donde se guardarán los archivos de registro generados por el logger.

logs_dir.mkdir(exist_ok=True) # Crea la carpeta logs si no existe, evitando errores si la carpeta ya está presente.

timestamp = datetime.now().strftime("%d%m%Y%H%M%S") # Obtiene la fecha y hora actual y la formatea como un string en el formato "DDMMYYYY HHMMSS", lo que permite nombrar los archivos de registro de manera única y organizada. FECHA Y HORA QUE SE EJECUTO.


# CONFIGURACION BASICA DEL LOGGER:
# es una función "logging.basicConfig" que le paso atributos entre parentesis para configurar el comportamiento del logger, como el nombre del archivo de registro, el nivel de registro y el formato de los mensajes de registro.
#Toma esto como configración PRINCIPAL del logger.
logging.basicConfig(
    filename=logs_dir / f"test_log_{timestamp}.log", # Especifica el nombre del archivo de registro, que se guardará en la carpeta "logs" con un nombre que incluye la fecha y hora de ejecución para facilitar su identificación. ARCHIVO UNICO.
    level=logging.INFO, # Establece el nivel de registro en INFO, lo que significa que se registrarán mensajes de información, advertencia, error y fallos críticos.
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", # define el formato de los mensajes de registro, que incluirá la fecha y hora del registro, el nivel de registro, el nombre del logger y el mensaje de registro. FORMATO en el que se va a almacenar todo CADA VEZ QUE INTERACTUA con el proyecto.
    #Ej. el 03/06/2026 20:45 hs estamos abriendo el navegador, el 03/06/2026 20:46 esta ingresando los datos de usuario y contraseña, el 03/06/2026 20:46 se hizo click en el boton de login, el 03/06/2026 20:48 se verifico que se ingreso correctamente a la pagina de inicio.
    force=True # Fuerza la configuración del logger incluso si ya se ha configurado previamente, lo que garantiza que la configuración definida en este bloque se aplique correctamente.
    )

#EJECUCION. Llamar al logger y lo ejecuta con el nombre que se le va asignar al proyecto.
logger = logging.getLogger("talento tech") # crea un logger con el nombre "talento tech", que se utilizará para registrar mensajes de registro relacionados con el proyecto. Este logger se puede usar en diferentes partes del código para registrar información relevante sobre la ejecución del proyecto, como eventos, errores, advertencias, etc. LOGGER ESPECIFICO PARA LOS TESTS.



