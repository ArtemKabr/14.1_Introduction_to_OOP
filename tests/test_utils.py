import os

from src.models import Product
from src.utils import load_data_from_json  # Убедись, что импорт верный


def test_load_data_from_json():
    test_file = os.path.join(os.path.dirname(__file__), "..", "products.json")
    categories = load_data_from_json(test_file)

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"

    # проверяем количество строк (товаров) в products
    assert len(categories[0].products) == 3

    # Проверка, что все продукты — экземпляры класса Product
    for product in categories[0].products:
        assert isinstance(product, Product)
