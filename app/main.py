from fastapi import FastAPI
from mangum import Mangum
from app.routers import greeting, calculator, text_processing, dynamodb
from app.core.logger import logger
from app.exceptions.handlers import http_exception_handler, validation_exception_handler
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Global exception handlers
app.add_exception_handler(Exception, http_exception_handler)
app.add_exception_handler(ValueError, validation_exception_handler)

# Register API routes
app.include_router(greeting.router, prefix="/greeting", tags=["Greeting"])
app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
app.include_router(text_processing.router, prefix="/text", tags=["Text Processing"])
app.include_router(dynamodb.router, prefix="/dynamodb", tags=["DynamoDB"])

# Integrate with AWS Lambda
handler = Mangum(app)

logger.info("Application has started.")
