import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_product_init(sample_products):
    product = sample_products[0]
    assert product.name == "Телефон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init(sample_category):
    assert sample_category.name == "Гаджеты"
    assert sample_category.products.count("\n") + 1 == 2


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


def test_product_str():
    product = Product("Test", "desc", 100.0, 3)
    assert str(product) == "Test, 100.0 руб. Остаток: 3 шт."


def test_category_str():
    p1 = Product("P1", "desc", 100.0, 1)
    p2 = Product("P2", "desc", 200.0, 2)
    category = Category("Категория", "описание", [p1, p2])
    assert str(category) == "Категория, количество продуктов: 3 шт."


def test_product_add():
    a = Product("A", "desc", 100.0, 5)
    b = Product("B", "desc", 200.0, 3)
    assert a + b == 8


def test_new_product_updates_existing(monkeypatch):
    # Автоматически подтверждаем изменение цены
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product1 = Product("Test", "desc", 100.0, 5)
    data = {"name": "Test", "description": "desc", "price": 150.0, "quantity": 2}
    result = Product.new_product(data, [product1])
    assert result.quantity == 7
    assert result.price == 150.0


def test_new_product_creates_new():
    data = {"name": "New Product", "description": "desc", "price": 150.0, "quantity": 3}
    result = Product.new_product(data, [])
    assert result.name == "New Product"
    assert result.quantity == 3
    assert result.price == 150.0


def test_add_same_type_smartphones():
    s1 = Smartphone("iPhone 15", "desc", 100000, 5, 95.0, "15", 256, "gray")
    s2 = Smartphone("Galaxy S23", "desc", 90000, 3, 94.0, "S23", 256, "black")
    result = s1 + s2
    assert result == 8


def test_add_same_type_grass():
    g1 = LawnGrass("Газон 1", "desc", 500, 10, "Россия", "5 дней", "Зеленый")
    g2 = LawnGrass("Газон 2", "desc", 450, 6, "США", "7 дней", "Темно-зеленый")
    result = g1 + g2
    assert result == 16


def test_add_different_types_raises():
    s = Smartphone("iPhone", "desc", 100000, 2, 90.0, "14", 128, "white")
    g = LawnGrass("Газон", "desc", 500, 3, "Казахстан", "4 дня", "Зеленый")
    with pytest.raises(TypeError):
        _ = s + g


def test_category_add_valid_product():
    s1 = Smartphone("iPhone", "desc", 100000, 1, 90.0, "14", 128, "white")
    category = Category("Смартфоны", "описание", [])
    category.add_product(s1)
    assert s1 in category._Category__products


def test_category_add_invalid_type_raises():
    category = Category("Смартфоны", "описание", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")  # строка, не Product


def test_product_zero_quantity_raises():
    """
    Проверяет, что при создании продукта с нулевым количеством возникает ValueError.
    """
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Пустой", "некорректный", 1000.0, 0)


def test_middle_price_empty_category_returns_zero():
    """
    Проверяет, что метод middle_price возвращает 0.0 для категории без продуктов.
    """
    empty_category = Category("Пустая", "без товаров", [])
    assert empty_category.middle_price() == 0.0
