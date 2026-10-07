class Pessoa:
    def __init__(self, nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.sexo = sexo
        self.cor = cor
        self.cpf = cpf
        self.cep = cep
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email, matricula, plano, forma_pagamento):
        super().__init__(nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email)
        self.matricula = matricula
        self.plano = plano
        self.forma_pagamento = forma_pagamento

class Personal(Pessoa):
    def __init__(self, nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email, salario, data_admissao, turno):
        super().__init__(nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email)
        self.salario = salario
        self.data_admissao = data_admissao
        self.turno = turno 

def Cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    altura = float(input("Digite a altura do aluno (em metros): "))
    peso = float(input("Digite o peso do aluno (em kg): "))
    sexo = input("Digite o sexo do aluno (M/F): ")
    cor = input("Digite a cor do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    cep = input("Digite o CEP do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    telefone = input("Digite o telefone do aluno: ")
    email = input("Digite o email do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    plano = input("Digite o plano do aluno: ")
    forma_pagamento = input("Digite a forma de pagamento do aluno: ")

    novo_aluno = Aluno(nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email, matricula, plano, forma_pagamento)
    
    return novo_aluno

def Cadastrar_personal():
    nome = input("Digite o nome do personal: ")
    idade = int(input("Digite a idade do personal: "))
    altura = float(input("Digite a altura do personal (em metros): "))
    peso = float(input("Digite o peso do personal (em kg): "))
    sexo = input("Digite o sexo do personal (M/F): ")
    cor = input("Digite a cor do personal: ")
    cpf = input("Digite o CPF do personal: ")
    cep = input("Digite o CEP do personal: ")
    endereco = input("Digite o endereço do personal: ")
    telefone = input("Digite o telefone do personal: ")
    email = input("Digite o email do personal: ")
    salario = float(input("Digite o salário do personal: "))
    data_admissao = input("Digite a data de admissão do personal: ")
    turno = input("Digite o turno do personal: ")

    novo_personal = Personal(nome, idade, altura, peso, sexo, cor, cpf, cep, endereco, telefone, email, salario, data_admissao, turno)

    return novo_personal



