Feature: Dividir dos numeros

    Scenario Outline: Suma
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: resta de Numeros
        | operacion  | num1 | num2 | result  |
        | dividir    | 2    | 2    | 1       |
        | dividir    | 4    | 2    | 2       |
        | dividir    | 1    | -1   | Invalid |