import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        prod = Product(price=2, weight=4)
        self.assertEqual(prod.stealability(), 'Kinda stealable')

    def test_explode(self):
        prod = Product(flammability=1, weight=4)
        self.assertEqual(prod.explode(), '...fizzle')


class AcmeReportTest(unittest.TestCase):
    def test_default_num_products(self):
        """Test generate 30 products"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test generated names"""
        prod_names = [prod.name for prod in generate_products()]
        for prod in prod_names:
            splt = prod.split()
            self.assertIn(splt[0], ADJECTIVES)
            self.assertIn(splt[1], NOUNS)

if __name__ == '__main__':
    unittest.main()
