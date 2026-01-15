# 1. Número divisible entre 3 y 5 la salida tiene que ser FizzBuzz
    def test_fizzbuzz_15(self):
        pass

    # 2. Número divisible entre 3 la salida tiene que ser Fizz
    def test_fizz_9(self):
        output = self.run_fizzbuzz(["9"])
        self.assertEqual(output, "Fizz")

    # 3. Número divisible entre 5 la salida tiene que ser Buzz
    def test_buzz_10(self):
        pass

    # 4. Número que no es múltiplo de 3 ni 5 la salida el propio número
    def test_normal_number(self):
        pass

    # 5. Límite inferior válido comprueba que el límite inferior funciona como entrada
    def test_lower_bound(self):
        output = self.run_fizzbuzz(["1"])
        self.assertEqual(output, "1")

    # 6. Límite superior válido comprueba que el límite superior funciona como entrada
    def test_upper_bound(self):
        pass

    # 7. Número menor que 1 (comprueba que de error por debajo del límite)
    def test_number_less_than_1(self):
        pass

    # 8. Número mayor que 100 (comprueba que de error por encima del límite)
    def test_number_greater_than_100(self):
        pass

    # 9. Entrada no numérica (texto)
    def test_non_numeric_input(self):
        pass

    # 10. Varios errores seguidos antes de entrada válida para comprobar el bucle
    def test_multiple_invalid_inputs(self):
        pass