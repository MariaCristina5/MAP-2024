import random
import string

def generare_parola(lungime, numere=True, caractere_speciale=True):
    litere = string.ascii_letters
    cifre = string.digits
    special = string.punctuation

    caractere = litere
    if numere:
        caractere += cifre
    if caractere_speciale:
        caractere += special
    parola=""
    valida = False
    are_numar = False
    are_special = False

    while not valida or len(parola) < lungime:
        caracter_nou = random.choice(caractere)
        parola += caracter_nou

        if caracter_nou in cifre:
            are_numar = True
        elif caracter_nou in special:
            are_special = True

        valida = True
        if numere:
            valida = are_numar
        if caractere_speciale:
            valida = valida and are_special
    return parola

lungime = int(input("Introdu numarul de caractere: "))
are_numar = input("Vrei sa contina cifre? (da/nu)").lower() == "da"
are_special = input("Vrei sa contina caractere speciale? (da/nu)").lower() == "da"


parola = generare_parola(lungime, are_numar, are_special)
print("Parola generata este:", parola)