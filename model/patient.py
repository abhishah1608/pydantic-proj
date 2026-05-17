from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give name of the patient in less than 50 characters', examples=['Abhi', 'John'])]
    age: int = Field(gt=0, lt=30)
    url : AnyUrl
    email : EmailStr
    occupation: Optional[str] = None 
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description="Is patient Married or not")]
    allergies: Annotated[Optional[List[str]], Field(max_length=5)]  
    contact_details: Dict[str, str]
    
    
    