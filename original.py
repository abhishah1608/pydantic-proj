from pydantic import AnyUrl, BaseModel, Field, field_validator
from typing import List, Dict, Optional, Annotated

from address import Address


class Patient(BaseModel):
    name: str
    age: int
    address: Address 
    url : AnyUrl
    email : str
    occupation: Annotated[Optional[str], Field(default=None, description="Occupation of the patient")] 
    weight: Annotated[float, Field(gt=0, strict=True, description="Weight of the patient in kg")]
    married: Annotated[bool, Field(default=None, description="Is patient Married or not")]
    allergies: Annotated[Optional[List[str]], Field(max_length=5)]  
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, value: str) -> str:
        valid_domains = ['example.com']
        domain = value.split('@')[-1];
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value
        
    
    @field_validator('name', mode='after')
    @classmethod
    def transform_name(cls, value: str) -> str:
        return value.title()
    
    @field_validator('age', mode='after')
    @classmethod    
    def validate_age(cls, value: int) -> int:
        if value <= 0 or value >= 30:
            raise ValueError("Age must be between 1 and 29")
        return value