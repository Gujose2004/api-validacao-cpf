from fastapi import FastAPI, HTTPException

app = FastAPI() # Criação da aplicação FastAPI

def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))   # Remove caracteres

    # Deve ter exatamente 11 dígitos
    if len(cpf) != 11:
       # print('CPF inválido, tente novamente')
        return False
    # Verifica se todos os dígitos são iguais - requerimento básico do CPF
    if cpf == cpf[0] * 11:
        return False
   
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    if int(cpf[9]) != digito1:
        return False
    
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    if int(cpf[10]) != digito2:
        return False
    return True
    
# Definição do endpoint para validar CPF
@app.get("/validar_cpf/{cpf}")
def validar_cpf_endpoint(cpf: str):
    if not validar_cpf(cpf):
        raise HTTPException(    
            status_code=202, detail={
                "valido": False,
                "mensagem":"CPF inválido"

                }
            
            )
    
    return{
        "cpf": cpf,
        "válido": True
    }
#uvicorn api:app --reload -> comando para rodar o servidor localmente
#uvicorn api:app --host 0.0.0.0 --port 8000 -> comando para rodar o servidor na rede local
#app.run(host="0.0.0.0", port=3000) fast
#uvicorn api:app --port 3000 --reload - comando para rodar