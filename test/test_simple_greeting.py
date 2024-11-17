from lambdas.simple_greeting import lambda_handler

def test_simple_greeting():
    event = {}
    context = None
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert "Hello" in response["body"]
