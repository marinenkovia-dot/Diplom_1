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

        assert burger.ingredients[0] is ing1

    def test_remove_last_ingredient(self):
        burger = Burger()
        ing0 = Mock()
        ing1 = Mock()
        burger.add_ingredient(ing0)
        burger.add_ingredient(ing1)

        burger.remove_ingredient(1)

        assert burger.ingredients[0] is ing0


class TestBurgerMoveIngredient:
    """Тесты перемещения ингредиентов"""

    @pytest.mark.parametrize("index,new_index,expected_order", [
        (0, 2, [1, 2, 0]),       # Переместить первый на третье место
        (2, 0, [2, 0, 1]),       # Переместить третий на первое место
        (0, 1, [1, 0, 2]),       # Переместить первый на второе место
        (1, 0, [1, 0, 2]),       # Переместить второй на первое место
    ])
    def test_move_ingredient(self, index, new_index, expected_order):
        burger = Burger()
        ing0 = Mock()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(index, new_index)

        ingredients = [ing0, ing1, ing2]
        expected = [ingredients[i] for i in expected_order]
        assert burger.ingredients == expected


class TestBurgerGetPrice:
    """Тесты расчёта цены"""

    def test_get_price_without_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 50.0
        burger.set_buns(bun)

        assert burger.get_price() == 100.0

    def test_get_price_one_ingredient(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 50.0
        burger.set_buns(bun)

        ing = Mock()
        ing.get_price.return_value = 50.0
        burger.add_ingredient(ing)

        assert burger.get_price() == 150.0

    def test_get_price_two_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 50.0
        burger.set_buns(bun)

        ing1 = Mock()
        ing1.get_price.return_value = 50.0
        ing2 = Mock()
        ing2.get_price.return_value = 30.0
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        assert burger.get_price() == 180.0

    def test_get_price_three_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 50.0
        burger.set_buns(bun)

        ing1 = Mock()
        ing1.get_price.return_value = 50.0
        ing2 = Mock()
        ing2.get_price.return_value = 30.0
        ing3 = Mock()
        ing3.get_price.return_value = 20.0
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        assert burger.get_price() == 200.0

    def test_get_price_different_bun_price(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 45.0
        burger.set_buns(bun)

        assert burger.get_price() == 90.0
