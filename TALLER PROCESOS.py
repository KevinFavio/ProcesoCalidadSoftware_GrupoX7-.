class Sintaxis:
    def usoIf(self,numero):
        if numero % 2 == 0:
            print("El numero {} es Par".format(numero))
        else:
             print("El numero {} es Impar".format(numero))

    def usoFor(self,dato):
        for ele in dato:
            print(ele,end="")
        print()    
        inicio = len(dato) -1
        for pos in range(inicio,-1,-1):
            print(pos,dato[pos],end=" ")
        print()    
        for pos,ele in enumerate(dato):
            print("[{}]={}".format(pos,ele))



    def usoWhile(self)
        numero = -1
        while numero < 0:
           numero = int(input("Ingrese numero positivo:  "))
        return numero

    def primo(self,num):
        cont = 2
        r=1
        while cont < num and r!=0:
            r = num % cont
            cont = cont +1
        return r                   

sintaxis = Sintaxis()
#sintaxis.usoFor("Hola")
#sintaxis.usoFor((10,"Hola",True,50.50))
#sintaxis.usoFor(["Dan",20,50.70])
num = 9
r= sintaxis.primo(num)
if r !=0:
    print("El numero:{} es primo".format(num))
else:
    print("El numero:{} no es primo".format(num))    
    
#lista = [2,5,7,10]
#for num in lista:
#   sintaxis.usoIf(num) 