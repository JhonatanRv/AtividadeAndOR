#Escreva um programa que peça ao usuário inserir três números e, em seguida, determine se um dos três números é maior que a soma dos outros dois.

var1 = float(input("Digite um número: "))
var2 = float(input("Digite outro número: "))
var3 = float(input("Digite mais um número: "))

if  var1 > var2 + var3 or var2 > var1 + var3 or var3 > var1 + var2:
    print("Dentro alguns dos números digitados é maior que a soma de outros dois números")

else: 
    print("Os números são iguais")

# Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine se o aluno passou ou não. Um aluno passa se a soma das notas for maior ou igual a 60 e nenhuma nota é menor que 40.

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))

soma = n1 + n2

if soma >= 60 and n1 >= 40 and n2 >= 40:
    print("O aluno foi aprovado")

else:
    print("O aluno foi reprovado")    

#Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.

idade = int(input("Digite a idade: "))
aut = input("Você possuí autorização? (s/n)")

if idade >= 18 or aut == "s":
    print("Você está aprovado para participar")

else:
    print("Você não tem autorização ou idade para participar")


#Escreva um código que verifique se um número é par ou divisível por 3.

num = int(input("Digite seu número: ")) 

if num % 2 == 0:
    print("Número digitado par")

elif num % 3  == 0:
    print("O número é divisível por 3")
else:
    print("O número é impar")

#Escreva um código que verifique se uma pessoa é alfabetizada (sabe ler e escrever) e tem mais de 25 anos de idade.
anos = int(input("Digite aqui a idade da pessoa"))    
alf = input("A pessoa possúi alfabetização? (s/n) ")

if idade > 25 and alf == "s":
    print("A pessoa é alfabetizada e possúi mais de 25 anos de idade")

else:
    print("A pessoa não atende aos critérios ")


# Criar um programa que verifica se uma pessoa tem desconto em um produto, baseado na idade e sua categoria (estudante, aposentado, etc.)
# e no dia da semana. (Use quantas categorias desejar)

idade = int(input("Digite aqui sua idade: "))
estado = input("Digite aqui se é estudante, aposentado, etc: ")
dia = input("Digite o dia da semana: ")

desc = 0 

if idade >= 60:
    desconto = 0.3
elif estado == "estudante" and (dia == "segunda" or dia == "terça"):
    desconto = 0.2
elif estado == "aposentado":
    desconto = 0.15
elif estado == "policial" and dia == "quarta":
    desconto = 0.25
