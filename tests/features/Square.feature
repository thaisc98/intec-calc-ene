Feature: Square of a number

    Scenario Outline: Square
        Given que quiero realizar operaciones aritméticas
        When desee <operation> <num1>
        Then the result will be <result>
        
        Examples: Square of a number
        | operation | num1  |  result |
        | Square     | 2    | 4       |
        | Square     | 4    | 16      |
        | Square     | 5    | 25      |
        | Square     | 10   | 100     |
        | Square     | -13  | Invalid |