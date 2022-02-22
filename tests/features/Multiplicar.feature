Feature: Multiplicar dos numeros

    Scenario Outline: Multiplicar
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: Multplicación de Numeros
        |operacion       | num1 | num2 | result  |
        | Multiplicación | 2    | 3    | 6       |
        | Multiplicación | 3    | 4    | 12      |
        | Multiplicación | 50   | 2    | 100     |
        | Multiplicación | 5    | 0    | 0       |
        | Multiplicación | 3    | -2   | Invalid |