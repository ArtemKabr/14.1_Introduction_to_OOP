from src.models import Category


def test_product_init(sample_products):
    product = sample_products[0]
    assert product.name == "Телефон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init(sample_category):
    assert sample_category.name == "Гаджеты"
    assert len(sample_category.products) == 2


def test_category_class_attributes(sample_category):
    assert Category.category_count == 1
    assert Category.product_count == 2
