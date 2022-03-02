Feature: Restar dos numeros

    Scenario: Resta
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: resta de Numeros
        | operacion | num1 | num2 | result  |
        | restar    | 2    | 2    | 0       |
        | restar    | 20   | 10   | 10      |
        | restar    | 100  | 300  | -200    |
        | restar    | 400  | 50   | 350     |
        | restar    | 1    | -1   | Invalid |