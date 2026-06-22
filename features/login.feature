@login
Feature: Inicio de sesion
    Background:
        Given que el usuario este en la pagina del Login

    @positivo
    Scenario: Login exitoso
        When ingresa el usuario 'standard_user' y contraseña 'secret_sauce'
        And hace clic en el boton Login
        Then deberia ingresar a la pagina del inventario

    @negativo
    Scenario: Login invalido con contraseña incorrecta
        When ingresa el usuario 'standard_user' y contraseña '12345'
        And hace clic en el boton Login
        Then deberia dar el mensaje de error 'Epic sadface: Username and password do not match any user in this service'

    @negativo @regression
    Scenario Outline: login invalido con diferentes usuarios
         When ingresa el usuario '<usuario>' y contraseña '<password>'
        And hace clic en el boton Login
        Then deberia dar el mensaje de error '<mensaje>'

        Examples:
            |usuario|password|mensaje|
            |standard_user|12345|Epic sadface: Username and password do not match any user in this service
            |stand_user|secret_sauce|Epic sadface: Username and password do not match any user in this service
            |VACIO|secret_sauce|Epic sadface: Username is required
            |standard_user|VACIO|Epic sadface: Password is required

            









