import secrets
from typing import List, Dict, Any

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

    # Logging
    LOGGING_CONFIG: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "class": "logging.Formatter",
                "format": "[%(asctime)s] %(levelname)s %(name)-15s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "detailed",
                "level": "DEBUG",
            },
        },
        "loggers": {
            "app.main": {"handlers": ["console"]},
            "app.api.api_v1.endpoints.upload": {"handlers": ["console"]},
            "app.calendar.html_parser": {"handlers": ["console"]},
        },
    }
    

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()