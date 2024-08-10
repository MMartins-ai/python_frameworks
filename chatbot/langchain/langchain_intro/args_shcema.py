from pydantic import BaseModel

class arg_schema_review(BaseModel):
    question: str

class arg_schema_waits(BaseModel):
    question: str