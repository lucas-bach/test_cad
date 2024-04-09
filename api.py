from fastapi import FastAPI, Query
import uvicorn
from typing import Union
from cadastro import insert_users, ler_csv
from typing import List



app = FastAPI()                                                        


@app.get("/consulte_10")
def home():
    dados_cvs = ler_csv()    
    return  dados_cvs[:10]

@app.get("/create_cad/{name}/{id}")
def create(name: str, id):
    insert_users()
    dados_cvs = ler_csv()    
    return  dados_cvs[:10]


@app.get("/consulte_by_name/{name}/{phone}/{cpf}/{sexo}/{state}/{namestate}/{city}")
def consulte(name,phone,cpf,sexo,state,namestate,city):
    dados_cvs = ler_csv()    
    return  dados_cvs[:10]


@app.get("/edit_name/{id}/{novo_nome}")
def edit(id, novo_nome):
    dados_cvs = ler_csv()    
    return  dados_cvs[:100]

@app.get("/delete_cad/{id}")
def delete():
    dados_cvs = ler_csv()    
    return  dados_cvs[:100]





# @app.get("/lista/{lista_id}")
# def pegar_item(lista_id:int):
#     if lista_id in cadastros:
#         return cadastros[lista_id]
#     else:
#         return{"Erro":"verifique o ID"}

# @app.get("/pesquisar/estado")
# def pesquisar_estado(estado: str = Query(..., description="Estado a ser pesquisado")):
#     resultado = pesquisar_por_estado(cadastros, estado)
#     return {"resultados": resultado}

# @app.get("/pesquisar/sexo")
# def pesquisar_sexo(sexo: str = Query(..., description="Sexo a ser pesquisado")):
#     resultado = pesquisar_por_sexo(cadastros, sexo)
#     return {"resultados": resultado} 


if __name__=="__main__":
    uvicorn.run(app)






