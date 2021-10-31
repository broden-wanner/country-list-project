from pydantic import BaseModel


class CountryListSchema(BaseModel):
    destination: str
    list: list[str]
