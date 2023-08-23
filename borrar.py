from pyrae import dle

def verificar_palabra(palabra):
    resultado = dle.search_by_word(word=palabra)
    return resultado.entries != []

palabra_a_verificar = "python"
if verificar_palabra(palabra_a_verificar):
    print(f'La palabra "{palabra_a_verificar}" está en el diccionario.')
else:
    print(f'La palabra "{palabra_a_verificar}" no está en el diccionario.')
