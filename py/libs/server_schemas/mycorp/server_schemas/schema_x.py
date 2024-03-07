from pydantic import BaseModel


class Stuff(BaseModel):
    mystr: str
    myints: list[int]

