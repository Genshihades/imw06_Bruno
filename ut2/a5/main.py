import sys
#ten cuidado no pongas ";" pon ":"
#número de vocales
def num_vowels(text):
    num_vowels = 0
    for char in text.lower():
        if char in "aeiouáéíóúü":
            num_vowels += 1
    return num_vowels

#número de espacios en blanco
def num_whitespaces(text):
    num_whitespaces = 0
    for char in text:
        if char in " ":
            num_whitespaces += 1
    return num_whitespaces
#Número de digitos
#fix Corregiste ; que pusistes en los números, recordado en la 2 linea
def num_digits(text):
    num_digits = 0
    for char in text:
        if char in "0123456789":
            num_digits += 1
    return num_digits
#Número de palabras
def num_words(text):
    docket = text.split()
    count = len(docket)
    return count
# lineas para darle la vuelta al texto.
def reverse(text):
    string = text
    text_rev = text[::-1]
    return text_rev
#Contador de tamaño
def length(text):
    num_char = len(text)
    return num_char
#Separador (gracias @sakurasensei)
def halfs(text):
    str_range = len(text)
    if str_range >= 2:
        mid = str_range // 2
        first_half = text[:mid]
        second_half = text[mid:]
    return " - ".join((first_half, second_half))
# v
def upper_vowels(text):
    vowels = "AEIOU"
    uppvow = ""
    for char in text:
        if char.upper() in vowels:
            uppvow += char.upper()
        else:
            uppvow += char
    return uppvow


def sorted_by_words(text):
    docket = text.split()
    docket.sort()
    sorted = ' '.join(docket)
    return sorted


#fix length of words(error en anterior linea 77 (aprende a escribir char que no es tan dificil -.-))
def length_of_words(text):
    text_docket = text.split()
    length_docket = []

    for char in text_docket:
        length = str(len(char))

        length_docket.append(length)
    word_len = " ".join(length_docket)

    return word_len


if __name__ == "__main__":
    text = sys.argv[1]
    print('Numero de vocales:', num_vowels(text))
    print('Numero de espacios:', num_whitespaces(text))
    print('Numero de digitos:', num_digits(text))
    print('Numero de palabras:', num_words(text))
    print('Texto al reves:', reverse(text))
    print('Largo del texto:', length(text))
    print('Texto cortado al medio:', halfs(text))
    print('Texto con las vocales en mayuscula:', upper_vowels(text))
    print('Ordenado por palabras:', sorted_by_words(text))
    print('Largo de las palabras:', length_of_words(text))



