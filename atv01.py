nota = int(input("digite a nota (entre 0 e 5):"))
while nota <0 or nota > 5 :
    print("nota invalida")
    nota = int(input("digite a nota novamente:"))
    print("nota valida")