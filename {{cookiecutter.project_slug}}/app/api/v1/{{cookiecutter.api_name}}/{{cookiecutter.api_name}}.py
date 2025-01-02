from fastapi import APIRouter, HTTPException
from schemas.schemas_name import schema1, schema2
from services.nome_do_arquivo import (
    svc_1, 
    svc_2
)

{{ cookiecutter.project_name }} = APIRouter()

#**
# @{{ cookiecutter.project_name }}.post
# @{{ cookiecutter.project_name }}.put
# @{{ cookiecutter.project_name }}.get
# @{{ cookiecutter.project_name }}.delete
#**

@{{ cookiecutter.project_name }}.post("/1")
async def svc_1_endpoint(schema: schema1):
    return await svc_1(schema)

@{{ cookiecutter.project_name }}.put("/2/{qqcoisa}")
async def svc_2_endpoint(qqcoisa: str, qqcoisa_data: schema2):
    return await svc_2(qqcoisa, qqcoisa_data)

