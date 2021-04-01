from pydantic import BaseModel

class Contact(BaseModel): 
    contact_id: int 
    first_name: str 
    last_name: str 
    user_name: str 
    password: str
    

contact_dict = {0:{'id':0, 
                    'first_name': 'KENNY',
                    'last_name':'MIRANDA',
                    'user_name':'kemirandad', 
                    'password':'Admin123'}}
