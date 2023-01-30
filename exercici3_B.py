"""Funció que demana al usuari l'edat e ingressos i ens dirá si podem fer o no la declaració d'hisenda"""

def exercici3B():
    edat= int(input("Introdueix la teva edat:"))
    ingressos= int(input("Indica els teus ingressos:"))
    if(edat>=18 and ingressos>1200):
        missatge= "És necessari que facis la declaració d’hisenda perquè tens {a} anys i tens uns ingressos de {b}".format(a=edat, b=ingressos)
    else:
        missatge= "Encara no pots fer la declaració"

    return missatge

print(exercici3B())
