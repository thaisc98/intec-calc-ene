import api
from fastapi.testclient import TestClient
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import parse

scenarios('Sumar.feature')

@given("que quiero realizar operaciones aritméticas", target_fixture="api_client")
def step_impl():
    return TestClient(api.app)

@when(
    parsers.cfparse("desee {operacion:String} {num1:Number} y {num2:Number}",
    extra_types=dict(Number=int, String=str)),
    target_fixture="calc_result",
)
def step_impl(api_client,operacion, num1, num2):
    api_result = api_client.get(f'/{operacion}?num1={num1}&num2={num2}')
    assert 200 == api_result.status_code
    return api_result.json().get('result')

@then(parsers.cfparse("el resultado debe ser {result}"))
def step_impl(calc_result,result):
    assert str(result) == str(calc_result)   