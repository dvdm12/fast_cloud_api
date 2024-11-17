from lambdas.basic_calculator import lambda_handler

def test_basic_calculator_addition():
    event = {"queryStringParameters": {"a": "3", "b": "5", "operator": "+"}}
    context = None
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert '"result": 8' in response["body"]

def test_basic_calculator_division_by_zero():
    event = {"queryStringParameters": {"a": "3", "b": "0", "operator": "/"}}
    context = None
    response = lambda_handler(event, context)
    assert response["statusCode"] == 400
    assert "Division by zero" in response["body"]
