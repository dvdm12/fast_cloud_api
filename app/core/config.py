import os

class Settings:
    PROJECT_NAME: str = "FastAPI AWS Lambda Project"
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    DYNAMODB_TABLE: str = os.getenv("DYNAMODB_TABLE", "Students")

settings = Settings()