class Calc:
    def sumar(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return "Invalid"
        return num1 + num2

    def divide(self, num1, num2):
        if num2 <= 0:
            return "Invalid"
        return num1 / num2