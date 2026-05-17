from original import Patient
from typing import Any

from address import Address

def insert_person(patient: Patient) -> None:
    print(patient.age)
    print(patient.name)
    print(patient.occupation)
    print(patient.weight)
    print(patient.married) 
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.email)         
    print(patient.url)
    print(patient.address)
    print(patient.address.full_address)
    
if __name__ == "__main__":
    address = {
    "street": "123 Main St",
    "city": "New York",    
    "state": "NY",
    "zipcode": "10001" 
    }
    
    patient_data : dict[str, Any] = {
        "name": "abhi shah",
        "age": '29',
        "occupation": "Software Engineer",
        "weight": 60.5,
        "married": False,
        "allergies": ["Peanuts", "Shellfish"],
        "contact_details": {"phone": "123-456-7890"},
        "email": "abhi.shah@example.com",
        'url' : 'https://a1.com',
        'address' : Address(**address)
        };
    
    patient = Patient(**patient_data)
    
    #insert_person(patient)
    
    dictstr = patient.model_dump()
    print("Dict string: ", dictstr)
     
    jsonstr = patient.model_dump_json()
    print("Json string: ", jsonstr)
    
    