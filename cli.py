import click
from pizza import Margherita, Hawaiian, Pepperoni
from order import delivery_order, bake, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    pizza = pizza.capitalize()
    if pizza not in ['Margherita', 'Pepperoni', 'Hawaiian']:
        print('Incorrect Pizza type')
        return
    bake(pizza)
    if delivery:
        delivery_order(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """Выводит меню"""
    pizza_types = {
        'Margherita 🧀': Margherita().recipe,
        'Pepperoni 🍕': Pepperoni().recipe,
        'Hawaiian 🍍': Hawaiian().recipe,
    }
    for key, value in pizza_types.items():
        print(f'- {key}: {", ".join([elem for elem in value])}')


if __name__ == '__main__':
    cli()
