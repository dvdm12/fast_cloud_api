from lambdas.dynamodb_connection import lambda_handler

def test_dynamodb_connection_valid_id(monkeypatch):
    # Mock os.getenv to return specific environment variables
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    monkeypatch.setenv("DYNAMODB_TABLE", "Students")

    # Mock boto3 DynamoDB response
    def mock_get_item(Key):
        if Key["id"] == "123":
            return {"Item": {"id": "123", "name": "John Doe"}}
        return {}

    class MockTable:
        def get_item(self, Key):
            return mock_get_item(Key)

    class MockDynamoDB:
        def Table(self, table_name):
            return MockTable()

    monkeypatch.setattr("boto3.resource", lambda service, region_name=None: MockDynamoDB())

    # Test the Lambda function
    event = {"queryStringParameters": {"id": "123"}}
    context = None
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert "John Doe" in response["body"]
