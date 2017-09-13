uval = input("Insira um valor: ")
try :
    xval = int(uval)
except:
    xval = -1

if xval > 0:
    print("O valor digitado foi", xval)
else:
    print("Digite um numero e tente novamente!")
