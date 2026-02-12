# Objetivo fazer uma calculadora para treinar lógica do While operadores: "+*/-"

while True:

    print("===BEM VINDO A WHILECALCULATOR===")
      
    print("\n---Escolha 1 para calcular---")
    print("\n---Escolha 2 para sair---")

    entrada = int(input(' Escolha a opção que se encaixe: '))
     
    while True:
        if entrada == 1:
            print('Operadores: +/-*')

            operador = input("Digite seu operador: ")
           
            valor1 = int(input('Digite um número: '))
            valor2 = int(input('Digite um outro número: '))

         try:
            if operador == +:
                soma = valor1 + valor2
                print('Resultado ', soma)

            elif operador == -:
                menos = valor1 - valor2
                print('Resultado ',  menos)
            
            elif operador == *:
                multiplicar = valor1 * valor2
                print('Resultado ',  multiplicar)

            elif operador == /:
                dividir = valor1 / valor2
                print('Resultado ',  dividir)

         except:
                print('Digite apenas inteiro')

        if entrada == 2:
            break
print(' ===FIM===')
break


                                      
