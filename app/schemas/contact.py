from pydantic import BaseModel, EmailStr, Field


class ContactRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    company: str | None = Field(default=None, max_length=150)
    service: str = Field(min_length=2, max_length=100)
    details: str = Field(min_length=10, max_length=3000)