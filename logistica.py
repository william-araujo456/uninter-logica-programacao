# Começo da função dimensoesObj
def dimensoesObj():
    while True:
        try:
            alt = int(input('Digite a altura do objeto (em cm): '))
            comp = int(input('Digite o comprimento do objeto (em cm):'))
            larg = int(input('Digite a largura do objeto (em cm):'))
            dimensoes = alt * comp * larg

            if dimensoes == dimensoes < 1000:
                return 10.00
            elif dimensoes == 1000 <= dimensoes < 10000:
                return 20.00
            elif dimensoes == 10000 <= dimensoes < 30000:
                return 30.00
            elif dimensoes == 30000 <= dimensoes < 100000:
                return 50.00
            else:
                dimensoes >= 100000 == print('Não aceitamos objetos com dimensões tão grandes!')
                continue
        except ValueError:
            continue


# Fim da função dimensoesObj

# Começo da função pesoObj
def pesoObj():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): '))

            if peso < 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            else:
                peso > 30 == print('Não aceitamos objetos tão pesados!')
                continue
        except ValueError:
            print('Você digitou o peso do objeto com valor não numérico')
            continue


# Fim da função pesoObj

# Começo da função rotaObj
def rotaObj():
    while True:
        rota = input(
            'Selecione a rota: \nAM- De Manaus para Macapá \nAC- De Manaus para Cuiabá \nCA- De Cuiabá para Manaus\nCM- De Cuiabá para Macapá \nMA- De Macapá para Manaus \nMC- De Macapá para Cuiabá\n>>>')

        if rota == 'AM':
            return 1
        if rota == 'AC':
            return 1
        if rota == 'CA':
            return 1.2
        if rota == 'CM':
            return 1.2
        if rota == 'MA':
            return 2
        if rota == 'MC':
            return 2
        else:
            print('Você digitou uma rota que não existe!')
            continue


# Fim da função rotaObj

# Começo da Main
print('Bem Vindo a Companhia de Logística de William Mattson S.A.')
dimensoes = dimensoesObj()
peso = pesoObj()
rota = rotaObj()
total = dimensoes * peso * rota
print('Total a pagar: R${} (dimensões: {} * peso: {} * rota: {}'.format(total, dimensoes, peso, rota))
# Fim da Main
