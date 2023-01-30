"""Funció per veure si un número es parell o imparell"""
def exercici2B():
    valor = int( input("Introdueix un valor: "))
    if valor % 2 == 0:
        missatge= "{num} és parell".format(num=valor)
    else:
        missatge= "{num} és senar".format(num=valor)

    return missatge


print(exercici2B())

