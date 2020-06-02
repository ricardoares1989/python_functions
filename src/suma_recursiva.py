
def suma_recursiva(a):
    b = input('Ingresa un numero para sumar o 0 para terminar: ')
    try:
        num = float(b)
        return suma_recursiva(a + num)
    except ValueError:
        return a
    





if __name__ == '__main__':
    print('SUMAR RECURISVAMENTE')
    a = float(input('Ingresa un numero a: '))    
    print(f'la suma de los numeros es {suma_recursiva(a)}')