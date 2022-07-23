#algoritimo para testar a classe desenvolvendo três objetos (contas de banco) para testar o código

from Desenvolvimento22 import Conta
import os
os.system('cls||clear')
cliente =[]
for i in range(3):
    Nome = str(input('Digite seu primeiro nome para criar uma conta \n'))
    Sobrenome = str(input('Digite seu sobrenome \n'))
    Numero = i+1
    Cpf = str(input('Digite o CPF do titular \n'))
    Saldo = float(input('Digite o valor do primeiro deposito \n'))
    Titular = Nome + " " + Sobrenome
    cliente.append(i)
    cliente[i] = Conta(Nome,Numero,Titular,Saldo,Cpf)
    os.system('cls||clear')


teste = 0
while teste != 5:
    num_cliente = int(input('Digite o numero do cliente \n'))
    num_cliente = num_cliente - 1
    os.system('cls||clear')
    teste = int(input('Digite a operação que deseja:\n 1. Ver dados \n 2. Saque\n 3. Deposito\n 4. Saldo\n 5. Sair\n"'))
    os.system('cls||clear')
    if teste == 1:
        cliente[num_cliente].dados()
    elif teste == 2:
        cliente[num_cliente].saque()
    elif teste == 3:
        cliente[num_cliente].deposito()
    elif teste == 4:
        cliente[num_cliente].saldo_atual()

          


