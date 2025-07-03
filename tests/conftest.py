import pytest

from src.models import Category, Product


@pytest.fixture
def sample_products():
    return [
        Product("Телефон", "Смартфон", 50000.0, 10),
        Product("Планшет", "iPad", 80000.0, 5),
    ]


@pytest.fixture
def sample_category(sample_products):
    Category.category_count = 0
    Category.product_count = 0
    return Category("Гаджеты", "Электроника", sample_products)
