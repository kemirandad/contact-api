from pydantic import BaseModel

class ContactUpdate(BaseModel): 
    first_name: str 
    last_name: str 
    user_name: str
    password: str