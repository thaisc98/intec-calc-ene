Feature: Square of a number

    Scenario Outline: Square
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: Potencia de nums
        | operacion | num1   | num2   |  result |
        | square     |  2    |   0    |    1    |
        | square     |  3    |   1    |    3    |
        | square     |  4    |   2    |    16   | 
        | square     |  5    |   3    |    125  | 
        | square     |  -2   |   2    | Invalid |