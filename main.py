# Escopo: Carro
# Atributos: id, modelo, marca, ano, valor, disponibilidade

from uuid import uuid4
from datetime import datetime

escopo = "carro"
atributos = ["id", "modelo", "marca", "ano", "valor", "disponibilidade"]    

carros = []
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
                buscarPorNome(lista)
            case 3:
                registrarLog(funcoes[opcao], lista_log)
                listarTodos(lista)
            case 4:
                registrarLog(funcoes[opcao], lista_log)
                listarDisponivel(lista)
            case 5:
                registrarLog(funcoes[opcao], lista_log)
                listarIndisponivel(lista)
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
                print('Contagem de carros')
            case 12:
                registrarLog(funcoes[opcao], lista_log)
                print(f'Busca por {atributos[1]}, {atributos[2]}')
            case 13:
                registrarLog(funcoes[opcao], lista_log)
                visualizarLog(lista_log)
            case 14:
                registrarLog(funcoes[opcao], lista_log)
                print('Lista ordenada')
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

def buscarPorNome(lista):
    print(f"--Buscar {escopo} por {atributos[1]}--")
    resultados = []

    isEmpty = verificaLista(lista)

    if not isEmpty:
        modelo = input("Digite o modelo desejado: ")

        for item in lista:
            if (modelo.lower() in item['modelo'].lower()):
                resultados.append(item)

        if (len(resultados) > 0):
            print(f"--Ocorrências encontradas--")

            for item in resultados:
                listarUnico(item)

def listarTodos(lista):
    print(f'--Todos os {escopo}s cadastrados--')
    
    isEmpty = verificaLista(lista)

    if not isEmpty:
        for item in lista:
            listarUnico(item)

def listarDisponivel(lista):
    print(f'--Todos os {escopo}s disponíveis--')
    resultados = []

    isEmpty = verificaLista(lista)

    if not isEmpty:
        for item in lista:
            if item['disponibilidade'] == True:
                resultados.append(item)

        if len(resultados) > 0:
            print(f'--Ocorrências encontradas--')

            for item in resultados:
                listarUnico(item)

def listarIndisponivel(lista):
    print(f'--Todos os {escopo}s indisponíveis--')
    resultados = []

    isEmpty = verificaLista(lista)

    if not isEmpty:
        for item in lista:
            if item['disponibilidade'] is not True:
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
        listarTodos(lista)
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
        listarTodos(lista)
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

def visualizarLog(lista_log):
    print('--Log de Acessos--')

    for item in lista_log:
        print(item)




menu(functions, carros, log)