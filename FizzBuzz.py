def fizzbuzz():
    entrada = input("Introduce un número entero positivo: ")

    if not entrada.isdigit():
        print("Error: debes introducir un número, no texto.")
        return

    n = int(entrada)

    if n <= 0:
        print("Error: el número debe ser mayor que 0.")
        return

    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()
