import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurgerInit:
    """Тесты инициализации класса Burger"""

    def test_init_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_init_ingredients_is_empty(self):
        burger = Burger()
        assert burger.ingredients == []


class TestBurgerSetBuns:
    """Тест установки булочки"""

    def test_set_buns(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun is bun
