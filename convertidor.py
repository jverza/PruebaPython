
def factorial(numero):
    numero_factorial = 1
    for i in range(1,numero):
        numero_factorial=numero_factorial*i
    return numero_factorial 


def primo(numero):
    numero_factorial=factorial(numero)
    aux=(numero_factorial+1)%numero
    if aux==0:
        return True
    else:
        return False


def run():
    numero = int(input("Ingerse un numero:"))
    contador =0
    for i in range(1,numero):
        if primo(i):
            print("El numero "+ str(i) + " es primo" )
            contador+=1
    print("Hay " + str(contador) + " numeros primos desde 1 a " + str(numero))



if __name__ == "__main__":
    run()


