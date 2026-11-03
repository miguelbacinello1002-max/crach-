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
