# Escopo: Carro
# Atributos: id, modelo, marca, ano, valor, disponibilidade

from uuid import uuid4
from datetime import datetime

escopo = "carro"
atributos = ["id", "modelo", "marca", "ano", "valor", "disponibilidade"]    

carros = [
    {"id": "f51f6753-dc17-4990-a84e-a915bc5278eb","modelo": "Jetta GLI", "marca": "Volkswagen", "ano": 2023, "valor": 250000, "disponibilidade": True},
    {"id": "67b5c27b-08f7-4e4a-a932-a5686f557fe4","modelo": "Polo GTS", "marca": "Volkswagen", "ano": 2023, "valor": 150000, "disponibilidade": True},
    {"id": "0a1a0555-b2f7-4a76-8978-24d3cc5b2131","modelo": "A3", "marca": "Audi", "ano": 2015, "valor": 90000, "disponibilidade": False},
    {"id": "270016ee-7c18-41fd-bc44-c3219b08362e","modelo": "Renegade Sport", "marca": "Jeep", "ano": 2023, "valor": 114000, "disponibilidade": False},
    {"id": "88e0d899-df60-47c1-a9a3-0d9b7b505be8","modelo": "Passat TSI", "marca": "Volkswagen", "ano": 2014, "valor": 76000, "disponibilidade": True},
]
log = []

functions = [
    "Sair",
    f"Cadastrar {escopo}",
    f"Buscar {escopo} por {atributos[1]}",
    f"Listar todos {escopo}s",
    f"Listar todos {escopo}s disponíveis",
    f"Listar todos {escopo}s indisponíveis",
    f"Atualizar {escopo}",
    f"Excluir {escopo}",
    f"Média de valor dos {escopo}s",
    f"{escopo} mais caro",
    f"{escopo} mais barato",
    f"Contagem de {escopo}s",
    f"Busca por {atributos[1], atributos[2]}",
    f"Log de acesso",
    f"Lista de {escopo}s ordenada",
]

def menu(funcoes, lista, lista_log):
    while True:
        print(f"--Concessionária de {escopo}s--")

        for item in funcoes:
            print(f"{funcoes.index(item)} - {item}")

        opcao = int(input("\n>>Escolha a opção desejada: "))
        
        match opcao:
            case 0:
                print("Encerrando a aplicação!")
                break
            case 1:
                registrarLog(funcoes[opcao], lista_log)
                cadastrar(lista)
            case 2:
                registrarLog(funcoes[opcao], lista_log)
                buscar(lista, 1)
            case 3:
                registrarLog(funcoes[opcao], lista_log)
                listar(lista, 1, None)
            case 4:
                registrarLog(funcoes[opcao], lista_log)
                listar(lista, 2, True)
            case 5:
                registrarLog(funcoes[opcao], lista_log)
                listar(lista, 2, False)
            case 6:
                registrarLog(funcoes[opcao], lista_log)
                atualizarCarro(lista)
            case 7:
                registrarLog(funcoes[opcao], lista_log)
                excluirCarro(lista)
            case 8:
                registrarLog(funcoes[opcao], lista_log)
                mediaValor(lista)
            case 9:
                registrarLog(funcoes[opcao], lista_log)
                porValor(lista, True)
            case 10:
                registrarLog(funcoes[opcao], lista_log)
                porValor(lista, False)
            case 11:
                registrarLog(funcoes[opcao], lista_log)
                contagem(lista)
            case 12:
                registrarLog(funcoes[opcao], lista_log)
                buscar(lista, False)
            case 13:
                registrarLog(funcoes[opcao], lista_log)
                visualizarLog(lista_log)
            case 14:
                registrarLog(funcoes[opcao], lista_log)
                listaOrdenada(lista)
            case _:
                registrarLog('Opção Inválida', lista_log)
                print("Opção inválida!")

def verificaLista(lista):
    if len(lista) <= 0:
        print("A lista está vazia!")
        return True
    else:
        return False

def registrarLog(funcao, lista_log):
    data = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    lista_log.append(f'{data} - {funcao}')

def cadastrar(lista):
    print(f'--Cadastro de {escopo}--')

    id = str(uuid4())
    modelo = input("Digite o modelo do carro: ")
    marca = input("Digite a marca do carro: ")
    ano = int(input("Digite o ano do carro: "))
    valor = float(input("Digite o valor do carro: "))
    disponibilidade = input("Digite a disponibilidade do carro (Sim / Não): ").lower().strip() == 'sim'

    carro = {
        atributos[0]: id,
        atributos[1]: modelo,
        atributos[2]: marca,
        atributos[3]: ano,
        atributos[4]: valor,
        atributos[5]: disponibilidade
    }

    lista.append(carro)
    print(f'{escopo} cadastrado com sucesso!')

def listarUnico(item):
        print('-' * 10)
        print(f"ID - {item['id']}")
        print(f"Modelo - {item['modelo']}")
        print(f"Marca - {item['marca']}")
        print(f"Ano - {item['ano']}")
        print(f"Valor - R${item['valor']}")
        if item['disponibilidade']:
            print(f"Disponibilidade - Sim")
        else:
            print(f"Disponibilidade - Não")

def buscar(lista, opcao):
    isEmpty = verificaLista(lista)

    if opcao == True:
        opcao = 1

    if not isEmpty:
        if opcao == False:
            print('1 para buscar por modelo, 2 para buscar por marca')
            opcao = int(input('Escolha a opção desejada: '))

        match opcao:
            case 1:
                print(f"--Buscar {escopo} por {atributos[1]}--")
                resultados = []
                modelo = input(f"Digite o {atributos[1]} desejado: ")

                for item in lista:
                    if (modelo.lower() in item['modelo'].lower()):
                        resultados.append(item)

                if (len(resultados) > 0):
                    print(f"--Ocorrências encontradas--")

                    for item in resultados:
                        listarUnico(item)

            case 2:
                print(f"--Buscar {escopo} por {atributos[2]}--")
                resultados = []
                modelo = input(f"Digite a {atributos[2]} desejado: ")

                for item in lista:
                    if (modelo.lower() in item['marca'].lower()):
                        resultados.append(item)

                if (len(resultados) > 0):
                    print(f"--Ocorrências encontradas--")

                    for item in resultados:
                        listarUnico(item)

            case _:
                print('Opção inválida')

def listar(lista, opcao, disponibilidade):
    isEmpty = verificaLista(lista)
    msg = ""

    if not disponibilidade:
        msg = 'in'

    if not isEmpty:
        match opcao:
            case 1:
                print(f'--Todos os {escopo}s cadastrados--')
                for item in lista:
                    listarUnico(item)
            
            case 2:
                print(f'--Todos os {escopo}s {msg}disponíveis--')
                resultados = []
                for item in lista:
                    if item['disponibilidade'] == disponibilidade:
                        resultados.append(item)

                if len(resultados) > 0:
                    print(f'--Ocorrências encontradas--')

                    for item in resultados:
                        listarUnico(item)

def atualizarCarro(lista):
    print(f'--Alterar dados de {escopo}--')

    isChanged = False
    isEmpty = verificaLista(lista)

    if not isEmpty:
        listar(lista, 1, None)
        idd = input('Digite o ID que deseja alterar: ')
        for item in lista:
            if idd == item['id']:
                print('Para não alterar a informação, mantenha a caixa de texto vazia')
                modelo = input("Digite o modelo do carro: ")
                marca = input("Digite a marca do carro: ")
                ano = int(input("Digite o ano do carro (0 para não alterar): "))
                valor = float(input("Digite o valor do carro (0 para não alterar): "))
                disponibilidade = input("Digite a disponibilidade do carro (Sim / Não): ").lower().strip() == 'sim'

                if modelo.strip() != "":
                    item['modelo'] = modelo
                if marca.strip() != "":
                    item['marca'] = marca
                if ano > 0:
                    item['ano'] = ano
                if valor > 0:
                    item['valor'] = valor
                if disponibilidade != item['disponibilidade']:
                    item['disponibilidade'] = disponibilidade

                print(f'{escopo} alterado com sucesso!')

                isChanged = True

        if not isChanged:
            print('ID não alterado/encontrado')


def excluirCarro(lista):
    print(f'--Excluir {escopo}')

    isDeleted = False
    isEmpty = verificaLista(lista)

    if not isEmpty:
        listar(lista, 1, None)
        idd = input('Digite o ID que deseja excluir(vazio para cancelar): ')
        if idd.strip() != "":
            for item in lista:
                if idd == item['id']:
                    lista.remove(item)
                    print(f'{escopo} excluído com sucesso!')
                    isDeleted = True

            if not isDeleted:
                print('ID não alterado/encontrado')
        
def mediaValor(lista):
    print(f'--Média de valores de {escopo}--')

    isEmpty = verificaLista(lista)

    if not isEmpty:
        soma = 0

        for item in lista:
            soma += item['valor']

        media = soma / len(lista)

        print(f'A média de valores dos R${escopo}s é de {media}')

def porValor(lista, ordem):
    isEmpty = verificaLista(lista)

    if not isEmpty:
        print(f'--{escopo.capitalize()} mais caro--')
        listaOrdenada = sorted(lista, key=lambda item: item['valor'], reverse=ordem)
        item = listaOrdenada[0]

        if ordem:
            msg = 'caro'
        else:
            msg = 'barato'

        print(f'O veículo mais {msg} é o {item["modelo"]}, custando R${item["valor"]}')

def contagem(lista):
    isEmpty = verificaLista(lista)

    if not isEmpty:
        print(f'--Contagem de {escopo}s')
        print(f'A quantidade de {escopo}s cadastrados é de {len(lista)}')

def listaOrdenada(lista):
    isEmpty = verificaLista(lista)

    if not isEmpty:
        opcao = int(input("1 para crescente, 2 para decrescente: "))

        match opcao:
            case 1:
                listaCrescente = sorted(lista, key=lambda item: item['modelo'])
                for item in listaCrescente:
                    listarUnico(item)
            case 2:
                listaDecrescente = sorted(lista, key=lambda item: item['modelo'], reverse=True)
                for item in listaDecrescente:
                    listarUnico(item)
            case _:
                print('Opção inválida')

def visualizarLog(lista_log):
    print('--Log de Acessos--')

    for item in lista_log:
        print(item)

menu(functions, carros, log)