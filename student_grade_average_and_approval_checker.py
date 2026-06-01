entrarousair=input("Digite entrar ou sair: ")
while entrarousair != "sair":
    n1=float(input("Digite a n1: "))
    n2=float(input("Digite a n2: "))
    n3=float(input("Digite a n3: "))
    
    media=(n1+n2+n3)/3
    if media > 70:
        print("Aprovado")
    else:
        print("Reprovado")
        
    entrarousair=input("Digite entrar ou sair: ")

print("Volte sempre!")