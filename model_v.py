from pydantic import AnyUrl, BaseModel, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: str
  age: int
  url : AnyUrl
  email : str
  occupation: Annotated[Optional[str], Field(default=None, description="Occupation of the patient", strict=True)]
  allergies: Optional[List[str]]
  contact_details: Dict[str, str]
  weight: Annotated[float, Field(gt=0, strict=True)]
  married: Annotated[bool, Field(default=None, description="Is patient Married or not")] 
  
  
  @model_validator(mode='after')
  @classmethod
  def validate_email(cls, model):
        valid_domains = ['example.com']
        domain = model.email.split('@')[-1];
        if domain not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return model