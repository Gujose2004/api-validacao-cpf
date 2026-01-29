def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))   # Remove caracteres

    # Deve ter exatamente 11 dígitos
    if len(cpf) != 11:
        print('CPF inválido, tente novamente')
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
         
if __name__ == "__main__":
    cpf_input = input("Digite o seu cpf:")
    if validar_cpf(cpf_input):
        print("CPF válido!")
    else:
       print("CPF inválido")
