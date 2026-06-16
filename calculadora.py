def calculadora():
    while True:
        print("\n=== Calculadora Básica ===")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "5":
            print("Encerrando a calculadora...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            print(f"Resultado: {num1 + num2}")
        elif escolha == "2":
            print(f"Resultado: {num1 - num2}")
        elif escolha == "3":
            print(f"Resultado: {num1 * num2}")
        elif escolha == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: divisão por zero não permitida.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()
