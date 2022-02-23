import unittest
from calc import Calc
from pytest_bdd import scenario, given, when, then, parsers
import parse

@scenario('Sumar.feature', 'Suma')
def test_calc():
    pass

@given("que quiero realizar operaciones aritméticas", target_fixture="calc")
def que_quiero_realizar_operaciones_aritmeticas():
    return Calc()

@when(
    parsers.cfparse("desee {operacion:String} {num1:Number} y {num2:Number}",
    extra_types=dict(Number=int, String=str)),
    target_fixture="calc_result",
)
def step_impl(calc,operacion, num1, num2):
    return calc.sumar(num1, num2)


@then(parsers.cfparse("el resultado debe ser {result}"))
def step_impls(calc_result,result):
    assert result == str(calc_result)