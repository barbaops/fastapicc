from pydantic import BaseModel
from typing import Optional

class schema1(BaseModel):
    name:        str
    mail:             str
    private:                Optional[str] = "private"
    bole:  Optional[bool] = False

class schema2(BaseModel):
    oopa:                Optional[str] = None
    oopo:         Optional[bool] = None