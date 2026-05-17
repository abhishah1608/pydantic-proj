from pydantic import BaseModel, Field, computed_field, field_validator
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    street : Annotated[str, Field(max_length=100, description="Street address of the patient", examples=['123 Main St', '456 Elm St'])]
    city: Annotated[str, Field(max_length=35, description="City of the patient", examples=['New York', 'Los Angeles'])]
    state: Annotated[str, Field(max_length=20, description="State of the patient", examples=['NY', 'CA'])]
    zipcode: str
    
    @field_validator('zipcode')
    @classmethod
    def validate_zipcode(cls, value: str) -> str:
        if not value.isdigit() or len(value) != 5:
            raise ValueError("Zipcode must be a 5-digit number")
        return value
    
    @computed_field
    def full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zipcode}"

            



