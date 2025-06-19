import os

from src.utils import load_data_from_json


def test_load_data_from_json():
    test_file = os.path.join(os.path.dirname(__file__), "..", "products.json")
    categories = load_data_from_json(test_file)

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 3
