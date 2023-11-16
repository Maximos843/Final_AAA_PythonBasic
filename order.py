import random
from typing import Callable, Union


def log(arg: Union[Callable, str]) -> Callable:
    if not callable(arg):
        def wrapper(func: Callable) -> Callable:
            def decorator(*args) -> str:
                return arg.format(args[0], func(*args))
            return decorator
        return wrapper
    else:
        def decorator(*args) -> str:
            return f'{arg.__name__} - {arg(args)}c!'
        return decorator


@log('👨‍🍳 Приготовили пиццу {} за {}с!')
def bake(pizza: str) -> int:
    """Готовит пиццу"""
    return random.randint(1, 5)


@log('🚀 Доставили пиццу {} за {}с!')
def delivery_order(pizza: str) -> int:
    """Доставляет пиццу"""
    return random.randint(1, 5)


@log('🛍 Забрали пиццу {} за {}с!')
def pickup(pizza: str) -> int:
    """Самовывоз"""
    return random.randint(1, 5)
