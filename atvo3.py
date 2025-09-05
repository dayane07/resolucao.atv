nome = (input("digite o nome do usuario:"))
senha = (input("digite a senha do usuario:"))

while nome != senha:
    print ("usuario e senha validos")
    break
else:
 while nome == senha: 
    print ("usuario e senha invalidos, tente novamente")
    nome = (input("digite o nome do usuario:"))
    senha = (input("digite a senha do usuario:"))
    

