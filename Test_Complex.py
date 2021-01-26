import unittest
from Complex_Library import *


class TestComplex(unittest.TestCase):

	def test_suma(self):
		c1 = (-7, -4)
		c2 = (3, -5)

		self.assertEqual(sumaComplejos(c1, c2), (-4, -9))


	def test_resta(self):
		c1 = (-3, 4)
		c2 = (3, 8)

		self.assertEqual(restaComplejos(c1, c2), (-6, -4))


	def test_producto(self):
		c1 = (3, -2)
		c2 = (1, 2)

		self.assertEqual(productoComplejos(c1, c2), (7, 4))


	def test_division(self):
		c1 = (-2, 1)
		c2 = (1, 2)

		self.assertEqual(divisionComplejos(c1, c2), 5)


	def test_modulo(self):
		c = (-7, 2)

		self.assertEqual(moduloComplejos(c), 7.28)


	def test_conjugado(self):
		c = (2, 4)

		self.assertEqual(conjugadoComplejos(c), (2, -4))


	def test_cart_polar(self):
		c = (1, 1)

		self.assertEqual(cartesiano_polar(c), (1.414, 45.000))


	def test_polar_cart(self):
		p = (math.sqrt(3), 80)

		self.assertEqual(polar_cartesiano(p), (0.301, 1.706))






if __name__ == '__main__':
    unittest.main()