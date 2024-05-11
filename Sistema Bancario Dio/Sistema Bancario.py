menu = """
[d] deposito
[s] saque
[e] extrato
[q] sair
=> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUE = 3
numero_saque = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito" ))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$: {valor:.2f}\n"

        else:
         print("Operação Falhou! Informe um valor Valido")
    
    elif opcao == "s":
       valor = float(input("Informe o valor de saque" ))

       excedeu_saldo = valor > saldo

       excedeu_limite = valor > limite

       execedeu_saque = numero_saque >= LIMITE_SAQUE



       if excedeu_saldo:
           print("Operação Falhou! Saldo Insuficiente")

       elif excedeu_limite:
           print("Operação Falhou! Valor excedeu o limite de saque diario")

       elif execedeu_saque:
           print("Operação Falhou! Numero de saques maximo excedido") 

       elif valor > 0:
          saldo -= valor
          extrato += f"\nSaque R$: {valor:.2f}\n"
          numero_saque += 1
      
       else:
          print("Operação Falhou! Informe um valor valido!")

    elif opcao == "e":
       print("\n============Extrato=============\n")
       print(f"Não foram feita movimentações\n " if not extrato else extrato)
       print(f"Saldo R$: {saldo:.2f}\n")
       print("================================\n")

    elif opcao =="q":
      break
    
    else:
       print("Operação Falhou! Informe uma opção valida!")
