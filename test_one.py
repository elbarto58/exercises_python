#02/10/2018
# 1. Largest product in a series

#función que nos devuelve la multiplicación mayor de todos
def get_result(number, k, length):
    aux = str(number) #convertimos nuestro numero a cadena para el facil manejo a la hora de extraer los numeros de acuerdo k
    flag = 0 #bandera que nos indicará cuando salir de nuestra iteracion
    x = 0 #contador para llevar el conteo de las iteraciones
    output = 0 #resultado
    while flag != 1: #mientras se siga cumpliendo esto
        count = x + k #esta suma indica cuantos caracteres tomar, para forma nuestro numero de acuerdo a k
        if count <= length: #para evitar acceder a un elemento que no existe
            new_number = aux[x:count] #nuevo  numero obtenido, el cual se multiplicará
            mult = 1 #inicializamos en 1 nuestra variable que llevará el resultado de nuestras multiplicaciones
            for j in range(k): #iteramos para multiplicar elemento por elemento de nuestro nuevo numero (que se obtuvo a partir de k)
                mult = mult * int(new_number[j]) #realizamos nuestra multiplicacion
            if output < mult: #comparamos para obtener el mayor resultado
                output = mult
            x = x + 1 #incrementamos nuestro contador
        else:
            flag = 1 #se esta tratando de acceder a indices que no existen, salimos de nuestro ciclo

    #regresamos la salida
    return output

#funcion principal
def test_one():
    try:
        t = int(input('')) #numero de tests
        if t >= 1 and t <= 100: #se cumplió que el numero de test esté en el rango
            results = [] #guardar mis resultados (outputs)
            for i in range(t): #la iteracion de acuerdo a t
                list_inputs = list(map(int, input().split())) #mis entradas
                if len(list_inputs) == 2: #Se cumplió que mis entradas sean de dos elementos
                    k = list_inputs[1] #obtenemos k
                    if k >= 1 and k <= 7: #se cumplió que k esté en el rango correcto
                        n = list_inputs[0]#obtenemos n
                        if n >= k and n <= 100: #se cumplió que n esté en el rango correcto
                            number = int(input('')) #ingresamos nuestro numero
                            length = len(str(number)) #obtenemos la longitud de nuestro numero capturado
                            if length == n: #se cumplió que nuestro numero tenga n digitos
                                output = 0  #inicializamos la varible de salida en 0
                                output = get_result(number, k, length) #cachamos el resultado que nos devuelve la funcion get_result
                                results.append(output) #agremos el resultadoa nuestra lista, y volvemos a empezar otra vez
                            else: #exit 5: numero de digitos de la entrada no coincide con n
                                print('- exit (5) -')
                        else: #exit 4: n no está en el rango correcto
                            print('- exit(4) -')
                    else: #exit 3: k no está en el rango correcto
                        print('- exit(3) -')
                else: #exit 2: el numero de entradas son diferentes de 2
                    print('- exit(2) -')
            for i in range(len(results)):
                print(results[i])    
        else: #exit 1: el numero de tests no está en el rango correcto
            print('- exit(1) -')
    except: #exit 0: ingrese una entrada correcta
        print('exit (0)')
        
