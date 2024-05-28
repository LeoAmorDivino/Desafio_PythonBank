saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3


while True:
    Operacao = int(input("Escolha o que deseja fazer:\n1 - Realizar um depósito\n2 - Realizar um saque\n3 - Verificar saldo\n"))

    if Operacao == 1:
        deposito = float(input("Qual o valor do depósito? "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

        else:
            print("O valor inserido não é compativel, tente novamente¹")
        
    elif Operacao == 2:
        saque =  float(input("Digite o valor que deseja retirar: "))

        
        excedeu_saldo = saque > saldo

        excedeu_limite = saldo > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
                print("O saldo não é suficiente. Tente novamente!.")

        elif excedeu_limite:
                print("O valor do saque excede o limite.")

        elif excedeu_saques:
                print("Número máximo de saques por hoje!. ")

        elif saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1

        else:
                print("O valor informado é inválido.")

    elif Operacao == 3:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    else:  print("Operação inválida, por favor selecione novamente a operação desejada.")
        

