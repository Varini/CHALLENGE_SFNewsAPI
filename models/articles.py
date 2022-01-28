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
            }
        }
