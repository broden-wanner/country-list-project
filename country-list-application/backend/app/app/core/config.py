import secrets
from typing import List

from pydantic import AnyHttpUrl, BaseSettings, BaseModel, EmailStr
from pydantic.tools import parse_obj_as

class Contact(BaseModel):
    url: AnyHttpUrl = parse_obj_as(AnyHttpUrl, "https://brodenwanner.com")
    name: str = "Broden Wanner"
    email: EmailStr = parse_obj_as(EmailStr, "brodenwanner@gmail.com")

class Settings(BaseSettings):
    PROJECT_NAME: str = "Country List Project"
    VERSION: str = "0.1.0"
    CONTACT: Contact = Contact()

    API_V1_STR: str = ""
    SECRET_KEY: str = secrets.token_urlsafe(32)

    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()