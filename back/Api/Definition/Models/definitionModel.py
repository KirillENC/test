from pydantic import BaseModel



class DefinitionModel(BaseModel):
    name: str
    value: str
