from bson import ObjectId
from typing import Optional, List
from pydantic import BaseModel, Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Launches(BaseModel):
    id: str = Field(...)
    provider: str = Field(...)


class Events(BaseModel):
    id: int = Field(...)
    provider: str = Field(...)


class Article(BaseModel):
    _id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    id: Optional[int]
    title: str = Field(...)
    url: str = Field(...)
    imageUrl: str = Field(...)
    newsSite: str = Field(...)
    summary: Optional[str]
    publishedAt: str = Field(...)
    updatedAt: str = Field(...)
    featured: bool = Field(...)
    launches: Optional[List[Launches]] = []
    events: Optional[List[Events]] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Article Title",
                "url": "Article URL",
                "imageUrl": "Article Image URL",
                "newsSite": "News Site Name",
                "summary": "",
                "publishedAt": "12-21-2021",
                "updatedAt": "01-01-2022",
                "featured": False,
                "launches": [
                    {
                        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "provider": "Provider Title"
                    }
                ],
                "events": [
                    {
                        "id": 0,
                        "provider": "Event Title"
                    }
                ],
            }
        }


class NewArticle(BaseModel):
    title: Optional[str]
    url: Optional[str]
    imageUrl: Optional[str]
    newsSite: Optional[str]
    summary: Optional[str]
    publishedAt: Optional[str]
    updatedAt: Optional[str]
    featured: Optional[str]
    launches: Optional[List[Launches]] = []
    events: Optional[List[Events]] = []

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "title": "Article Title",
                "url": "Article URL",
                "imageUrl": "Article Image URL",
                "newsSite": "News Site Name",
                "summary": "",
                "publishedAt": "12-21-2021",
                "updatedAt": "01-01-2022",
                "featured": False,
                "launches": [
                    {
                        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "provider": "Provider Title"
                    }
                ],
                "events": [
                    {
                        "id": 0,
                        "provider": "Event Title"
                    }
                ],
            }
        }
