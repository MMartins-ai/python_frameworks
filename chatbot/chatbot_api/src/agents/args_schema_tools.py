from pydantic import BaseModel
from typing import Any

class schema_reviews_vector_chain(BaseModel):
    question: str


class schema_hospital_cypher_chain(BaseModel):
    question: str


class schema_get_current_wait_times(BaseModel):
    hospital: str


class schema_generico(BaseModel):
    any: Any