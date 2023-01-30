"""Funció que demanarà a l'usuari dos valors, els compararà i retornarà el valor petit i gran"""

def exercici1B():
    #Input per preguntar a l'usuari 2 números:
    valor1 = input("Introdueix un número: ")
    valor2 = input("Ara introdueix un altre valor: ")
    if (valor1>valor2):
        missatge = ('El valor més gran és: {a} i el valor més petit és: {b}'.format(a=valor1, b=valor2))

    if (valor2>valor1):
        missatge = ('El valor més gran és: {a} i el valor més petit és: {b}'.format(a=valor2, b=valor1))


    return missatge
print (exercici1B())