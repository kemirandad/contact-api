from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

from Model.contact_in import Contact, contact_dict
from ModelOut import contact_out

app = FastAPI()

@app.get("/") 
def home(): 
    return contact_dict

@app.post('/contact', 
          response_model=Contact,
          response_model_exclude={"password"}, 
          description='Cree un solo usuario')
async def create_contact (contact: Contact): 
    if contact.contact_id < 1:
        raise HTTPException(status_code=404, detail='Contact id error')
    elif contact.contact_id in contact_dict:
        raise HTTPException(status_code=404, detail='Contact id already exist')
    else:
        contact_dict[contact.contact_id] = {'id':contact.contact_id, 
                                            'first_name': contact.first_name,
                                            'last_name':contact.last_name,
                                            'user_name':contact.user_name, 
                                            'password':contact.password}
        return contact

@app.get('/contact/{contact_id}', 
         response_model_exclude={"password"})
async def read_contact(contact_id: int):
    if contact_id not in contact_dict:
        raise HTTPException(status_code=400, detail='Contact id not found')
    else:
        return {'user_name':contact_dict[contact_id]['user_name'],
                'first_name':contact_dict[contact_id]['first_name'],
                'last_name':contact_dict[contact_id]['last_name']}
    
@app.put('/contact/{contact_id}',
         description='Actualiza un solo contacto')
async def update_contact(contact: Contact):
    if contact.contact_id in contact_dict:
        if contact.password == contact_dict[contact.contact_id]['password']:
            contact_dict[contact.contact_id] = {'first_name': contact.first_name,
                                            'last_name':contact.last_name,
                                            'user_name':contact.user_name, 
                                            'password':contact.password}
            return {'Done':'Contact updated satisfactorily'}
        else:
            raise HTTPException(status_code=400, detail='Password incorrect')
    else:
        raise HTTPException(status_code=400, detail='Contact id not found')
    
@app.delete('/contact/{contact_id}', 
         response_model_exclude={"password"})
async def delete_contact(contact: Contact):
    contact_values = [int(contact.contact_id), 
                      contact.first_name, 
                      contact.last_name,
                      contact.user_name, 
                      contact.password]
    contact_dict_values = list(contact_dict[contact.contact_id].values())
    if contact_values == contact_dict_values:
        contact_dict.pop(contact.contact_id)
        return {'Done':'Contact delected satisfactorily'}
    else:
        raise HTTPException(status_code=400, detail='Contact id not found')
