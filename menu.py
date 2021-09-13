from validacao import Validacao

def menu(opcao):
    
    if opcao == 1:
        informacao = get('e-mail')
        Validacao.validaEmail(informacao)
        return 0

    if opcao == 2:
        informacao = get('CPF')
        Validacao.validaCpf(informacao)
        return 0

    if opcao == 3:
        informacao = get('CNPJ')
        Validacao.validaCnpj(informacao)
        return 0
        
    if opcao == 4:
        return 1

# Getter
def get(informacao):
        return input(f'Digite o seu {informacao}: ')


while True:
    print('Selecione uma opção de validação: \n[1] Validar Com e-mail\n[2] Validar de CPF\n[3] Validar com CNPJ\n[4]Sair: \n\nOpção desejada: ')
    opcaoDesejada = input()

    if menu(opcaoDesejada) == 1:
        break