from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products():
    products = []
    for i in range(30):
        name = '{}{}'.format(sample(ADJECTIVES, k=1)[0],
                             sample(NOUNS, k=1)[0])
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = float('{0:.2f}'.format(uniform(0.0, 2.5)))
        prod = Product(name=name, price=price, weight=weight,
                       flammability=flammability)
        products.append(prod)
    return products


def inventory_report(products):
    prod_name = [prod.name for prod in products]
    print("Unique Product names: ", len(set(prod_names)))

    avg_price = sum([prod.price for prod in products]) / len(products)
    avg_wieght = sum([prod.weight for prod in products]) / len(products)
    avg_flammability = sum([prod.flammability for prod in products]) / len(products)

print("="*42)
print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
print("="*42)
print(f'Average Price: {avg_price:.2f}')
print(f'Average Weight: {avg_weight:.1f} lb')
print(f'Average Flammability: {avg_flammability:.2f}')

if __name__ = '__main__':
    inventory_report(generate_products())
