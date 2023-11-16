class Pizza:
    def __init__(self, recipe: list[str] = [], size: str = 'L'):
        self.recipe = recipe
        self.size = size

    def __eq__(self, other_pizza):
        if not isinstance(other_pizza, Pizza):
            raise TypeError("Некорректный параметр для сравнения пицц")
        return (sorted(self.recipe) == sorted(other_pizza.recipe))\
            and (self.size == other_pizza.size)


class Margherita(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(['tomato sauce', 'mozzarella', 'tomatoes'], size)


class Pepperoni(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(['tomato sauce', 'mozzarella', 'pepperoni'], size)


class Hawaiian(Pizza):
    def __init__(self, size: str = 'L'):
        super().__init__(['tomato sauce', 'mozzarella', 'chicken', 'pineapples'], size)
