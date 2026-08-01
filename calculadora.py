cond = "s"
while cond == "s":
      num = int(input("Digite um número: "))
      num2 = int(input("Digite um segundo número: "))

      print("Seu primeiro número foi ",num)
      print("Seu segundo número foi ",num2)

      print("Escolha uma Operação: 1- Soma, 2- Subtração, 3- Multiplicação, 4- Divisão")
      operacao = input("Digite o número ao lado: ")

      if operacao == "1":
            resultado = num + num2
            print("Resultado dos números é ",resultado)
      elif operacao == "2":
            resultado = num - num2
            print("Resultado dos números é ",resultado)
      elif operacao == "3":
            resultado = num * num2
            print("Resultado dos números é ",resultado)
      elif operacao == "4":
            if num2 == 0:
                print("O número não pode ser dividido por 0")
            else:        
                resultado = num / num2
                print("Resultado dos números é ",resultado)
      else:
            print("nenhuma opção válida")
      cond = input("Deseja fazer outra conta? (s/n): ")
print("Até mais, tchau tchau!")
