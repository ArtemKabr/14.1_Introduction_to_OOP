import os
from src.utils import load_data_from_json  # Убедись, что импорт верный


def test_load_data_from_json():
    test_file = os.path.join(os.path.dirname(__file__), "..", "products.json")
    categories = load_data_from_json(test_file)

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"

    # проверяем количество строк (товаров) в products
    product_lines = categories[0].products.strip().split("\n")
    assert len(product_lines) == 3
