import json
from typing import List
from src.models import Product, Category


def load_data_from_json(file_path: str) -> List[Category]:
    """
    Загружает список категорий и товаров из JSON-файла.
    """
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for category_data in data:
        products = [Product(**prod) for prod in category_data["products"]]
        category = Category(category_data["name"], category_data["description"], products)
        categories.append(category)

    return categories
