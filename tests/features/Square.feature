Feature: Square of a number

    Scenario Outline: Square
        Given that I want to make math operation
        When <operation> <num1> <>
        Then the result will be <result>
        
        Examples: Square of a number
        | operation | num1  |  result |
        | Square     | 2    | 4       |
        | Square     | 4    | 16      |
        | Square     | 5    | 25      |
        | Square     | 10   | 100     |
        | Square     | -13  | Invalid |