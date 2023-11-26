import unittest
from pizza import Margherita, Pepperoni, Hawaiian


class TestPizza(unittest.TestCase):

    def test_equal_pizza_equal(self):
        margherita1 = Margherita(size='XL')
        margherita2 = Margherita(size='XL')
        self.assertEqual(margherita1, margherita2)

    def test_different_size_equal(self):
        margherita1 = Margherita(size='L')
        margherita2 = Margherita(size='XL')
        self.assertEqual(margherita1, margherita2)

    def test_different_types(self):
        margherita = Margherita(size='L')
        pepperoni = Pepperoni(size='XL')
        self.assertNotEqual(margherita, pepperoni)

    def test_hawaiian_wrong_size(self):
        with self.assertRaises(ValueError):
            Hawaiian('S')

    def test_pepperoni_wrong_size(self):
        with self.assertRaises(ValueError):
            Pepperoni('S')

    def test_margherita_wrong_size(self):
        with self.assertRaises(ValueError):
            Margherita('S')

    def test_dict_hawaii(self):
        self.assertEqual(
            Hawaiian('L').dict(),
            {'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}
        )

    def test_dict_pepperoni(self):
        self.assertEqual(
            Pepperoni('L').dict(),
            {'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']}
        )

    def test_dict_margherita(self):
        self.assertEqual(
            Margherita('L').dict(),
            {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']}
        )
