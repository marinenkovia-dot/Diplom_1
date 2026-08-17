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


class TestBurgerAddIngredient:
    """Тесты добавления ингредиентов"""

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] is ingredient

    def test_add_multiple_ingredients(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        ing3 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        assert burger.ingredients == [ing1, ing2, ing3]


class TestBurgerRemoveIngredient:
    """Тесты удаления ингредиентов"""

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient_by_index(self, index):
        burger = Burger()
        ing0 = Mock()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(index)

        assert len(burger.ingredients) == 2

    def test_remove_first_ingredient(self):
        burger = Burger()
        ing0 = Mock()
        ing1 = Mock()
        burger.add_ingredient(ing0)
        burger.add_ingredient(ing1)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ing1

    def test_remove_last_ingredient(self):
        burger = Burger()
        ing0 = Mock()
        ing1 = Mock()
        burger.add_ingredient(ing0)
        burger.add_ingredient(ing1)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ing0
