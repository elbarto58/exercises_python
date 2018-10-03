#02/10/2018
#2. Largest palindrome product

#función que me devuelve si el numero de entrada es un palidromo o no
def get_if_is_palindrome(number):
    aux = str(number) #convertimos nuestra entrada en cadena para voltear la cadena y hacer la comparacion para verificar si es o no un palindromo
    if aux == aux[::-1]: #comparando si es un palindromo o no (arreglo[::-1] esta sentencia nos voltea el arreglo que le indicamos, por ejemplo 'Hola', aplicando esa sentencia obtendríamos 'aloH')
        #regresamos una verdadero (Si es palindromo)
        return True
    #regresamos un falso (No es palindromo)
    return False

#función principal
def test_two():
    try:
        t = int(input('')) #numero de tests
        if t >= 1 and t <= 100: #se cumplió que el numero de test esté en el rango
            results = []
            for i in range(t):
                n = int(input(''))
                if n > 101101 and n < 1000000:
                    final_result = 0
                    for num_one in range(100,999):#numero 1 de 3 digitos
                        for num_two in range(100,999):#numero 2 de 3 digitos
                            result = num_one * num_two
                            if result < n:
                                if get_if_is_palindrome(result):
                                    if final_result < result:
                                        final_result = result

                    results.append(final_result)

                else: #exit 2: n no está en el rango correcto
                    print('exit (2)')
            for j in range(len(results)):
                print(results[j])

        else: #exit 1: el numero de tests no está en el rango correcto
            print('exit (1)')
    except: #exit 0: ingrese una entrada correcta
        print('exit (0)')
