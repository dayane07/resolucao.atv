nota = (0, 1, 2, 3, 4, 5)
if nota >= 0 and nota <= 5:
    int(input("digite a nota:"))
    print ("digite a nota:")
    print ("nota valida")

else: 
    while nota < 0 or nota > 5: 
        print ("nota invalida")
        nota = int(input("digite a nota:"))
    