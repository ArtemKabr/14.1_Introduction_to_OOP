import pytest
from src.models import Product, Category

from src.models import Category


def test_product_init(sample_products):
    product = sample_products[0]
    assert product.name == "Телефон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init(sample_category):
    assert sample_category.name == "Гаджеты"
    assert sample_category.products.count("\n") + 1 == 2


def test_category_class_attributes(sample_category):
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_product_increases_count(sample_category):
    product = Product("Наушники", "Bluetooth", 3000, 5)
    initial_count = Category.product_count
    sample_category.add_product(product)
    assert Category.product_count == initial_count + 1



def test_products_getter_format(sample_category):
    result = sample_category.products
    assert "Телефон" in result
    assert "руб." in result
    assert "Остаток" in result


def test_new_product_creates_new():
    product_list = []
    data = {
        "name": "Планшет",
        "description": "10-дюймовый экран",
        "price": 25000.0,
        "quantity": 4
    }
    new_p = Product.new_product(data, product_list)
    assert isinstance(new_p, Product)
    assert new_p.name == "Планшет"


def test_new_product_updates_existing():
    existing = [Product("Планшет", "Старое", 20000.0, 2)]
    data = {"name": "Планшет", "description": "Новое", "price": 30000.0, "quantity": 3}
    updated = Product.new_product(data, existing)
    assert updated.quantity == 5
    assert updated.price == 30000.0


def test_price_setter_valid(monkeypatch):
    product = Product("Камера", "HD", 15000, 3)
    product.price = 17000
    assert product.price == 17000


def test_price_setter_invalid(capsys):
    product = Product("Камера", "HD", 15000, 3)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000


def test_price_setter_decrease_confirm(monkeypatch):
    product = Product("Камера", "HD", 15000, 3)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 12000
    assert product.price == 12000

    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 10000
    assert product.price == 12000  # не изменилось
