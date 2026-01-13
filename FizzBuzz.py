def fizzbuzz():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 100: "))

            if n < 1 or n > 100:
                print("Error: el número debe estar entre 1 y 100.")
                continue

            break 

        except ValueError:
            print("Error: debes introducir un número entero, no texto.")

    
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

fizzbuzz()
