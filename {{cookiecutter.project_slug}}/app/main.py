from fastapi import FastAPI
from api.v1.{{cookiecutter.api_name}}.routes import {{cookiecutter.api_name}}

app = FastAPI(title="AWS Bucket Manager API", version="1.0")

app.include_router({{cookiecutter.api_name}}, prefix="/api/v1/aws/bucket", tags=["AWS"])
