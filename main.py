"""from fastapi import FastAPI
app = FastAPI()
item_venda = {
    1: {"item": "coca-cola", "preco_unitario": 5, "quantidade": 5},
    2: {"item": "cerveja 600ml", "preco_unitario": 10, "quantidade": 5},
    3: {"item": "vinho 750ml", "preco_unitario": 30, "quantidade": 5},
    4: {"item": "gin", "preco_unitario": 100, "quantidade": 5},
}

@app.get("/")
def home():
    return {"APP de Vendas com FastAPI"}

@app.get("/item_venda/{id_venda}")
def selelcionar_venda_por_id(id_venda: int):
    return item_venda[id_venda]"""
    

"""from fastapi import FastAPI
app = FastAPI()
@app.get("/item/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}"""
"""
from fastapi import FastAPI
app = FastAPI()
@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id} """   


from fastapi import FastAPI
app = FastAPI()
#    
#POST
"""@app.post("/postdata/")
def post_data(nome_do_usuario: str):
    lista_de_nomes.append(nome_do_usuario)
    return {
        "nome_do_usuario":lista_de_nomes} 
#"""
#GET
@app.get("/getdata/{nome_do_usuario}")
def get_data(nome_do_usuario: str):
    return {
        "nome": nome_do_usuario} 
#POST
@app.post("/postdata/")
def post_data(nome_do_usuario: str):
    return {
        "nome": nome_do_usuario}
#PUT
lista_de_nomes=[]
@app.put("/putdata/{nome_do_usuario}")
def put_data(nome_do_usuario: str):
    print(nome_do_usuario)
    lista_de_nomes.append(nome_do_usuario)
    return {
        "nome_do_usuario":lista_de_nomes} 
#DELETE
@app.delete("/deletedata/{nome_do_usuario}")
def delete_data(nome_do_usuario: str):
    lista_de_nomes.remove(nome_do_usuario)
    return {
        "nome_do_usuario":lista_de_nomes} 


