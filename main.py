numero = (input("Digite um número: "))
numero = int(numero)
 
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")

else:
    if numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
