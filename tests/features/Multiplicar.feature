Feature: Multiplicar dos numeros

    Scenario Outline: multiplicar
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: Multplicación de Numeros
        |operacion       | num1 | num2 | result  |
        | multiplicar | 2    | 3    | 6       |
        | multiplicar | 3    | 4    | 12      |
        | multiplicar | 50   | 2    | 100     |
        | multiplicar | 5    | 0    | 0       |
        | multiplicar | 3    | -2   | Invalid |