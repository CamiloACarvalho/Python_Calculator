resultado = 0

a = float (input())

while True:

    ope = input()
    b = 0
    
    if ope == "+":

        b = float (input())
        resultado = resultado+a+b
        a=0
        print (resultado)
        

    elif ope == "-":

        b = float (input())
        resultado = a-b+resultado
        a=0
        print (resultado)
    
    elif ope == "*":

        b = float (input())
        resultado = (resultado*b)+(a*b)
        a=0
        print (resultado)

    elif ope == "/":
        b = float (input())
        resultado = (resultado/b)+(a/b)
        a=0
        print (resultado)

    elif ope == "=":
        
        break
    

print (resultado)