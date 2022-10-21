import pytest


class Factory:

    def bake_cake(self, toppings: int, base: int) -> int:
        amount = 0
        if toppings == base == 1:
            amount = 1
        elif toppings == base:
            amount = toppings // 5 + toppings % 5 // 2 + toppings % 5 % 2
        return amount

    def get_last_cakes(self, n: int) -> list:
        pass

    def get_cakes_baked(self) -> list:
        pass

    def __str__(self):
        return


class Cake:

    def __init__(self, base_amount, toppings_amount):
        allowed_list = [1, 2, 5]
        if base_amount not in allowed_list and toppings_amount not in allowed_list:
            raise WrongIngredientsAmountException("Incorrect amount of ingredients!")
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount

    @property
    def type(self):
        if self.base_amount == 1 and self.toppings_amount == 1:
            return "basic"
        elif self.base_amount == 2 and self.toppings_amount == 2:
            return "medium"
        elif self.base_amount == 5 and self.toppings_amount == 5:
            return "large"

    def __repr__(self):
        return f"Cake({self.type})"

    def __eq__(self, other):
        return self.type == other.type


class WrongIngredientsAmountException(Exception):
    pass
