from fastapi import HTTPException
from schema.{{cookiecutter.schemas_name}} import (
    schema1, 
    schema2
)

s3_client = boto3.client("s3")

async def create(valor: schema1):
    try:
        #Logica da criacao

        return {"message": f"created successfully"}
    except ClientError as e:
        raise HTTPException(status_code=400, detail=str(e))

async def update_bucket(valor_passado: str, valor_data: schema2):
    try:
        #Logica do update
        return {"message":f"updated successfully"}
    except ClientError as e:
        raise HTTPException(status_code=400, detail=str(e))
