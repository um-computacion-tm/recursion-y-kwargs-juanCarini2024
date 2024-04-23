import unittest

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n -1) + fibonacci(n -2) 

class Testfibonacci(unittest.TestCase):

    def test1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 0)

    def test4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 2)

    def test5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 3)    

    def test8(self):
        resultado = fibonacci(8)
        self.assertEqual(resultado, 13)

    def test9(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 21)   

    def test10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 34) 

    def test12(self):
        resultado = fibonacci(12)
        self.assertEqual(resultado, 89)            


unittest.main()


