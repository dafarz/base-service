from pydantic import BaseModel


class Test(BaseModel):
    id: int
    text: str
