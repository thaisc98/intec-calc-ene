Feature: Power of a number

    Scenario Outline: Power
        Given que quiero realizar operaciones aritméticas
        When desee <operacion> <num1> y <num2>
        Then el resultado debe ser <result>
        
        Examples: Potencia de nums
        | operacion  | num1  | num2   |  result |
        | power     |  2    |   0    |    1    |
        | power     |  3    |   1    |    3    |
        | power     |  4    |   2    |    16   | 
        | power     |  5    |   3    |    125  | 
        | power     |  -2   |   2    | Invalid |