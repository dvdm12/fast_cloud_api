FastAPI AWS Lambda Project

A serverless application built with FastAPI, deployed on AWS Lambda, and integrated with API Gateway. This project demonstrates modular API development, including endpoints for greetings, a calculator, text processing, and DynamoDB operations. The repository is configured for automated deployments using GitHub Actions.
Features

    🚀 FastAPI Framework: Build fast, modern, and interactive APIs.
    ☁️ AWS Lambda Integration: Serverless architecture with seamless scalability.
    🌐 API Gateway: Expose HTTP endpoints for your APIs.
    📂 DynamoDB Support: Easily query and store data with AWS DynamoDB.
    🔧 Centralized Configuration: Manage environment variables and settings in one place.
    📊 Logging and Error Handling: Centralized logging and consistent error responses.
    🤖 Automated Deployments: GitHub Actions workflow for CI/CD.
    🧪 Unit Testing: Ensure code reliability with tests for all endpoints.

Project Structure

/fastapi-project
├── app/
│   ├── main.py               # Entry point for FastAPI application
│   ├── routers/              # API endpoints
│   │   ├── greeting.py       # Endpoint for greetings
│   │   ├── calculator.py     # Endpoint for calculator operations
│   │   ├── text_processing.py # Endpoint for text processing
│   │   ├── dynamodb.py       # Endpoint for DynamoDB operations
│   ├── core/                 # Core configurations and utilities
│   │   ├── config.py         # Centralized settings
│   │   ├── logger.py         # Logging setup
│   ├── exceptions/           # Global exception handling
│   │   ├── handlers.py       # Custom exception handlers
│   └── tests/                # Unit tests for the application
├── venv/                     # Virtual environment (ignored by Git)
├── requirements.txt          # Dependencies
├── build.sh                  # Script to package the project for AWS Lambda
├── .github/workflows/        # GitHub Actions workflow
│   └── deploy-lambdas.yml    # Automated deployment workflow
├── README.md                 # Project documentation
├── .gitignore                # Files and directories to ignore in Git

Endpoints
Greeting API

    GET /greeting/
        Returns a simple greeting message.
        Example Response:

    { "message": "Hello, welcome to the system!" }

GET /greeting/{name}

    Returns a personalized greeting message.
    Example Response:

        { "message": "Hello, John!" }

Calculator API

    GET /calculator/
        Performs arithmetic operations.
        Query Parameters: a, b, operator (+, -, *, /).
        Example Request:

/calculator/?a=5&b=3&operator=+

Example Response:

        { "result": 8 }

Text Processing API

    POST /text/
        Processes a given text.
        Request Body:

{ "text": "FastAPI is amazing!" }

Example Response:

        {
          "word_count": 3,
          "character_count": 19,
          "uppercase_text": "FASTAPI IS AMAZING!"
        }

DynamoDB API

    GET /dynamodb/{id}
        Fetches an item from the DynamoDB table.
        Example Response:

        { "id": "123", "name": "John Doe", "score": 95 }

Setup and Installation
1. Clone the Repository

git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project

2. Create and Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run Locally

Start the server with Uvicorn:

uvicorn app.main:app --reload

Access the API documentation at:

    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

Deployment
1. Build the Project for AWS Lambda

Run the build.sh script to package the application and its dependencies:

./build.sh

This creates a app.zip file for deployment.
2. Deploy with GitHub Actions

The repository includes a GitHub Actions workflow (.github/workflows/deploy-lambdas.yml) that automates deployment to AWS Lambda. Push changes to the main branch to trigger the workflow.

Ensure AWS credentials are added as secrets in the GitHub repository:

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_REGION

Testing
Run Unit Tests

Tests are located in the app/tests/ directory. Use pytest to execute them:

pytest app/tests/

Example Test File:

test_greeting.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_simple_greeting():
    response = client.get("/greeting/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, welcome to the system!"}

Project Configuration

    Configuration File: app/core/config.py
    Environment Variables:
        AWS_REGION: Default AWS region (e.g., us-east-1).
        DYNAMODB_TABLE: Name of the DynamoDB table.

Contributing

    Fork the repository.
    Create a new branch for your feature:

git checkout -b feature-name

Commit your changes and push:

    git add .
    git commit -m "Add feature-name"
    git push origin feature-name

    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Let me know if you'd like help customizing this README further! 🚀
