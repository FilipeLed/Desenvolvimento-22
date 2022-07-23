#Classe para gerar contas bancarias de clientes, conferir dados, ver saldo, sacar e depositar


class Conta:
    def __init__(self,nome,numero,titular,saldo,cpf):
        self.nome = nome
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.cpf = cpf
        
    def saldo_atual(self):
        print(f'Saldo: R${self.saldo}')

    def dados(self):
        print(f'Titula: {self.titular}')
        print(f'CPF: {self.cpf}')
        print(f'Saldo: R${self.saldo}')

    def deposito(self):
        valor_deposito = float(input('Digite o valor do deposito \n'))
        self.saldo = self.saldo + valor_deposito
        return self.saldo

    def saque(self):
        valor_saque = float(input('Digite o valor do saque \n'))
        if (valor_saque < self.saldo):
            self.saldo = self.saldo - valor_saque
            return self.saldo
        else:
            print('\n Saldo insuficiente')

