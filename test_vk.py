import pytest


class TestVk:
    tpl: tuple = (1,)
    int_digit: int = 2

    def test_check_int_no_dot(self):
        """ Тест проверяет, что целое число не является числом с плавающей точкой. """
        assert '.' not in str(self.int_digit)

    def test_check_int(self):
        """ Тест проверяет, что число является целым а не вещественным. """
        assert self.int_digit == int(self.int_digit)

    @pytest.mark.parametrize("given,expected", [(5, int), ((1,), tuple)])
    def test_check_tuple_and_int(self, given, expected):
        """ Тест проверяет на тип данных. """
        assert isinstance(given, expected)

    def test_get_element_tuple(self):
        """ Тест проверяет получение элемента из кортежа по индексу. """
        assert self.tpl[0] == 1

    def test_change_tuple(self):
        """ Тест проверяет невозможность изменения элемента в кортеже. """
        try:
            self.tpl[0] = 6
        except TypeError as e:
            assert True
