# HOOK globales: son funciones especiales que se ejecutan antes o después de ciertos momentos clave durante la ejecución de las pruebas.


from selenium import webdriver


# ABRO EL NAVEGADOR (driver) y se ejecuta segun cada escenario definido en el archivo .feature
def before_scenario(context,scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()




# CIERRO EL NAVEGADOR (driver) al finalizar cada escenario definido en el archivo .feature
def after_scenario(context,scenario):
    context.driver.quit()


