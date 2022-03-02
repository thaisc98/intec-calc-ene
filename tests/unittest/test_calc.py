import unittest
from calc import Calc
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import parse

scenarios('Sumar.feature')
scenarios('Restar.feature')
scenarios('Square.feature')

@given("que quiero realizar operaciones aritméticas", target_fixture="calc")
def step_impl():
    return Calc()

@when(
    parsers.cfparse("desee {operacion:String} {num1:Number} y {num2:Number}",
    extra_types=dict(Number=int, String=str)),
    target_fixture="calc_result",
)
def step_impl(calc,operacion, num1, num2):
    if operacion == "sumar":
        return calc.sumar(num1, num2)
    elif operacion == "restar":
        return calc.restar(num1, num2)

@then(parsers.cfparse("el resultado debe ser {result}"))
def step_impl(calc_result,result):
    assert result == str(calc_result)

@when(
      parsers.cfparse("desee {operation:String} {num1:Number}",
    extra_types=dict(Number=int, String=str)),
    target_fixture="calc_result"
)
def step_impl(calc, operation, num1): 
    if operation == "square":
        return calc.square(num1)

@then(parsers.cfparse("the result will be {result}"))
def step_impl(calc_result, result):
    assert result == str(calc_result)

