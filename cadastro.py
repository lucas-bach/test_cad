from pydantic import BaseModel

class Cadastro(BaseModel):
    name: str
    phone: str
    cpf: str
    sexo: str
    state: str
    namestate: str
    city: str

def pesquisar_por_estado(cadastros, estado, limite = 10):
    resultados = []
    encontrados = 0
    
    for cadastro in cadastros:
        if cadastro["state"] == estado:
            resultados.append(cadastro)
            encontrados += 1
            
            if encontrados == limite:
                break
    
    return resultados


def pesquisar_por_sexo(cadastros, sexo, limite = 10):
    resultados = []
    encontrados = 0
    
    for cadastro in cadastros:
        if cadastro["sexo"] == sexo:
            resultados.append(cadastro)
            encontrados += 1
            
            if encontrados == limite:
                break
    
    return resultados


with open("lista.csv", 'r') as file:
    linhas = file.readlines()

cadastros = []

for linha in linhas[1:]:
    campos = linha.strip().split(",")
    
    state = campos[4].strip('()').replace("'", "")
    namestate = campos[5].strip('()').replace("'", "").replace(" ", "")
    
    cadastro = {
        "name": campos[0],
        "phone": campos[1],
        "cpf": campos[2],
        "sexo": campos[3],
        "state": state,
        "namestate": namestate,
        "city": campos[6],
    }
    
    cadastros.append(cadastro)




# with open("lista.csv", 'r') as file:
#     linhas = file.readlines()


# cadastros = []


# for linha in linhas[1:]:    
#     campos = linha.strip().split(",")

#     state = campos[4].strip('()').replace("'", "")
#     namestate = campos[5].strip('()').replace("'", "").replace(" ", "")
    
#     cadastro = {
#         "name": campos[0],
#         "phone": campos[1],
#         "cpf": campos[2],
#         "sexo": campos[3],
#         "state": state,
#         "namestate": namestate,
#         "city": campos[6],

#     }   


#     cadastros.append(cadastro)


# for i, cadastro in enumerate(cadastros[:50]):
#     print(f"Cadastro {i+1}: {cadastro}")



# estado_desejado = "SC"
# contatos_encontrados = 0
# contatos_estado = []



# for cadastro in cadastros:
    
#     if cadastro["state"] == estado_desejado:
        
#         contatos_encontrados += 1
        
#         contatos_estado.append(cadastro)
        
        
#         if contatos_encontrados == 10:
#             print("Final da lista!")
#             break


# for i, contato in enumerate(contatos_estado):
#     print(f"Contato {i+1}: {contato}")

# genero_masculino = "M"
# usuarios_encontrados = 0
# usuarios_masculinos = []    

# print("\nUsuários masculinos:")
# for cadastro in cadastros:

#     if cadastro["sexo"] == genero_masculino:

#         usuarios_encontrados += 1

#         usuarios_masculinos.append(cadastro)

#         if usuarios_encontrados == 10:    
#             break

# for i, contato in enumerate(usuarios_masculinos):
#     print(f"Contato {i+1}: {contato}")


