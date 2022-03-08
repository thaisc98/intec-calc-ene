Feature: Residuo de dos numeros

    Scenario Outline: Residuo
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: Residuo de Numeros
        | operacion | num1 | num2 | result  |
        | restar    | 2    | 5    | 2       |
        | restar    | 10   | 2    | 0       |
        | restar    | 20   | 6    | 2       |
        | restar    | 33   | 7    | 5       |
        | restar    | 60   |-1    | Invalid |
