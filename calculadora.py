# Objetivo fazer uma calculadora para treinar lógica do While operadores: "+*/-"

while True:
    print("===BEM VINDO A WHILECALCULATOR===")
      
    print("\n---Escolha 1 para calcular---")
    print("\n---Escolha 2 para sair---")

   try: 

     entrada = int(input(' Escolha a opção que se encaixe: '))
          
              
     if entrada == 1:
       print('Operadores: +/-*')

       operador = input("Digite seu operador: ")
                                            
       valor1 = int(input('Digite um número: '))
       valor2 = int(input('Digite um outro número: '))



                                                    
        if operador == "+":
                soma = valor1 + valor2
                print('Resultado ', soma)

       elif operador == "-":
                menos = valor1 - valor2
                print('Resultado ',  menos)
            
       elif operador == "*":
                multiplicar = valor1 * valor2
                print('Resultado ',  multiplicar)

       elif operador == "/":
                dividir = valor1 / valor2
                print('Resultado ',  dividir)

       else:
        print('Isso nao é um operador')

    if entrada == 2:
      print(' FIMFIM===')
      
          break

   except ValueError:
         print('Digite apenas inteiro')




                                      
