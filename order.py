import random
from typing import Callable


def log(template: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def decorator(*args, **kwargs) -> str:
            res = func(*args, **kwargs)
            print(template.format(args[0], random.randint(1, 5)))
            return res
        return decorator
    return wrapper


@log('👨‍🍳 Приготовили пиццу {} за {}с!')
def bake(pizza: str):
    """Готовит пиццу"""
    pass


@log('🚀 Доставили пиццу {} за {}с!')
def delivery_order(pizza: str):
    """Доставляет пиццу"""
    pass


@log('🛍 Забрали пиццу {} за {}с!')
def pickup(pizza: str):
    """Самовывоз"""
    pass
