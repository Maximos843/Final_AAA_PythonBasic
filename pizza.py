from typing import Optional


class Pizza:
    def __init__(self, name: str = '', recipe: Optional[list[str]] = None, size: str = 'L'):
        if size not in ['XL', 'L'] or\
              name not in ['Margherita', 'Pepperoni', 'Hawaiian']:
            raise ValueError
        self.size = size
        self.name = name
        if recipe is None:
            self.recipe = []
        else:
            self.recipe = recipe

    def dict(self) -> dict[str, list[str]]:
        return {self.name: self.recipe}

    def __eq__(self, other_pizza) -> bool:
        if not isinstance(other_pizza, Pizza):
            raise NotImplementedError
        return self.name == other_pizza.name


class Margherita(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(
            'Margherita', ['tomato sauce', 'mozzarella', 'tomatoes'], size
        )


class Pepperoni(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(
            'Pepperoni', ['tomato sauce', 'mozzarella', 'pepperoni'], size
        )


class Hawaiian(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(
            'Hawaiian', ['tomato sauce', 'mozzarella', 'chicken', 'pineapples'], size
        )
