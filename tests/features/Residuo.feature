Feature: Residuo de dos numeros

    Scenario Outline: Residuo
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: residuo de Numeros
        | operacion  | num1 | num2 | result  |
        | residuo    | 2    | 5    | 2       |
        | residuo    | 10   | 2    | 0       |
        | residuo    | 20   | 6    | 2       |
        | residuo    | 33   | 7    | 5       |
        | residuo    | 1    | -1   | Invalid |
