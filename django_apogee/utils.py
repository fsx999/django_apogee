# coding=utf-8
from __future__ import unicode_literals


def make_etudiant_password(p_numetu):
    code_ied = str(p_numetu)
    if p_numetu == "":
        return None
    longeur_code = len(code_ied)
    if longeur_code > 6:
        indice = longeur_code - 6
        code_ied = code_ied[indice:]
    #    code_ied = str(p_numetu)
    longeur_code = len(code_ied)
    if longeur_code < 4:  # si le code est moins de 4 chiffre, on compléte avec zéro
        code_ied = "0" * (4 - longeur_code) + code_ied
        longeur_code = 4
    som = 0
    for i in code_ied:
        som += int(i)  # somme des nombres du code
    tbc = [0] * 11  # cle de cryptage
    bcl1 = int(p_numetu)
    for i in range(1, 11):  # on remplit la cle de cryptage
        bcl1 = bcl1 + (i * longeur_code) + som
        tbc[i] = bcl1
    a1 = int(code_ied[-1:]) + 1
    b1 = int(code_ied[-2:-1]) + 1
    c1 = int(code_ied[-3:-2]) + 1
    d1 = int(code_ied[-4:-3]) + 1
    a2 = ((a1 * b1) % 3) + 1
    b2 = ((b1 * c1) % 7) + 1
    c2 = ((c1 * d1) % 11) + 1
    d2 = ((d1 * a1) % 17) + 1
    code = (a2 * tbc[a1]) + b2 * tbc[b1] + (c2 * tbc[c1]) + (d2 * tbc[d1])
    if code > 9999:  # ici on s'assure que le code soit bien de 4 chiffre
        if code % 10000 == 0:
            code += 45
        code %= 10000
    if code < 10:
        code *= 817
    if code < 100:
        code *= 71
    res100 = code / 100
    if code % 100 == 0:
        if code < 5000:
            code += (res100 * som)
        else:
            code -= (res100 * som)
    code = str(code)
    if len(code) != 4:
        code = "0" + code
    return code
