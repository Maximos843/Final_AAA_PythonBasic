import unittest
from pizza import Margherita


class TestPizza(unittest.TestCase):

    def test_equal_pizza(self):
        margherita1 = Margherita(size='XL')
        margherita2 = Margherita(size='XL')
        self.assertEqual(margherita1, margherita2)

    def test_different_size(self):
        margherita1 = Margherita(size='L')
        margherita2 = Margherita(size='XL')
        self.assertNotEqual(margherita1, margherita2)

    def test_different_types(self):
        margherita = Margherita(size='L')
        pepperoni = Margherita(size='XL')
        self.assertNotEqual(margherita, pepperoni)
