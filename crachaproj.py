print("----------------------------------------")
print("        Bem vindo, trabalhador          ")
print("----------------------------------------")

nome = input("Solicite seu nome:  ")
cargo = input("Informe seu cargo: ")

print("-------------------------------------------------------------------")
print(f" Olá {nome}, você é um(a) {cargo} e está registrado(a) no sistema.")
print("-------------------------------------------------------------------")

hora = float(input("Qual é o valor de sua hora de trabalho?: "))
dia = float(input("Quantas horas você trabalha por dia?: "))
horas_extras = float(input("Quantas horas extras você trabalhou?: "))
horas = dia * hora * 15 + horas_extras * hora
print(f" ---Você recebe um valor de R$ {horas}.---") 

print("-----------------------------------------")
print("         Gastos  de viagem...            ")
print("-----------------------------------------")

transporte = float(input("Qual é o valor gasto com transporte?: "))
alimentacao = float(input("Qual é o valor gasto com alimentação?: "))
hospedagem = float(input("Qual é o valor gasto com hospedagem?: "))

gastos = transporte + alimentacao + hospedagem
print(f" ---Você gastou um total de R$ {horas - gastos} nessa viagem.---") 

print("---------------------")
print("### NOSSOS GASTOS ###")
print("---------------------")


produtos_novos = float(input("Qual é o valor desse produto que está nos oferencendo?: "))
por_produtosnovos = produtos_novos * 0.35
print(f" ---Temos que ter um ganho de R$ {por_produtosnovos} nesse produto.---")


print("----------------------------------------")
print("         Controle de acesso...          ")
print("----------------------------------------")


idade = int(input("Informe a sua idade: "))
 
if idade < 15 or idade > 24 :
    print("Acesso negado.")
    False
else:
    True
    print("Acesso liberado")


print("----------------------------------------")
print("         Controle de credencial...      ")
print("----------------------------------------")


credencial = input("Informe a sua credencial(ativa/bloqueada): ").strip().lower()
 
if credencial == "bloqueada":
    print("Credencial bloqueada")
    
elif credencial == "ativa":
    print("Credencial aceita")


preço_empresa = float(input("Qual é o preço do produto que a empresa está oferecendo?: "))
if preço_empresa >= 100000:
    print("Aprovamos limite de até 20.000")
elif preço_empresa > 50000 and preço_empresa < 100000:
    print("Aprovamos limite de até 10.000")
else:
    print("Crédito reprovado, o valor do produto é muito baixo para aprovação de crédito.")


faltas = int(input("Digite o número de faltas injustificadas: "))
vendas = float(input("Digite o valor total de vendas: R$ "))
 
 
if faltas == 0 and vendas > 50000:
    print("PLR Aprovada")
else:
    print("PLR Negada")



print("----------------------------------------")
print( "               Sua região              ")
print("----------------------------------------")

regiao = input("Informe a sua região(S,SE,CO,NE,E): ").strip().upper()
if regiao == "S" or regiao == "SE":
    print(" Sua taxa de frete é de 15R$")
elif regiao == "NE" or regiao == "N":
    print(" Sua taxa de frete é de 35R$")
elif regiao == "CO":
    print(" Sua taxa de frete é de 25R$")


print ("======================")
print ("ESTOQUE DE PRODUTOS   ")
print ("======================")
print("")
estoque = int(input("informe a quanidade de produtos no estoque: "))
if estoque <16:
    print("COMPRA URGENTE")
if estoque >16 and estoque < 50:
    print("ESTOQUE REGULAR")
if estoque > 50:
    print("ESTOQUE CHEIO")


while True:
    matricula = input("Digite a matrícula do funcionário para bater o ponto: ").strip()
   
   
    if matricula == "0000":
        print("Sistema encerrado para manutenção.")
        break
       
   
    print(f"Ponto batido com sucesso para a matrícula: {matricula}!")
    print("-" * 30)




funcionarios = ["ana", "lucas", "beatriz", "carlos"]
 
 
for nome in funcionarios:
   
    email = f"{nome.strip().lower()}@arketech.com"
    print(f"Funcionário(a): {nome.title()} -> E-mail: {email}"




senha = "Admin123"
tentativas = 1
max_tentativas = 3
 
while tentativas <= max_tentativas:
    print(f"Tentativas {tentativas} de {max_tentativas}")
    senha_digitada = input("Digite a sua senha: ")
    if senha_digitada == senha:
     print("Acesso liberado")
     break
    else:
     print("Senha INCORRETA")
     print("Tente novamente")
     tentativas += 1
else:
    print("Acesso bloqueado")
 



tri_um = input("Digite a quantidade de vendas do 1º trimestre: ")
tri_dois = input("Digite a quantidade de vendas do 2º trimestre: ")
tri_tres = input("Digite a quantidade de vendas do 3º trimestre: ")
print(f" O total dos três trimestres é: {float(tri_um) + float(tri_dois) + float(tri_tres)}")