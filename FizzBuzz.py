def fizzbuzz(n: int) -> str:
    if n < 1 or n > 100:
        raise ValueError("El número debe estar entre 1 y 100")

    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

while True:
    try:
        n = int(input("Introduce un número entero entre 1 y 100: "))
        print(fizzbuzz(n))
        break
    except ValueError as e:
        print("Error:", e)
