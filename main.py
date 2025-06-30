import os
import sys

from src.models import Category, Product
from src.utils import load_data_from_json

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))


def main() -> None:
    """
    Основная точка входа: загружает данные из products.json
    и выводит информацию о категориях и товарах.
    """
    json_path = os.path.join(os.path.dirname(__file__), "products.json")
    categories = load_data_from_json(json_path)

    print("\n📦 Категории и товары:\n")
    for category in categories:
        print(f"🔹 Категория: {category.name}")
        print(f"   Описание: {category.description}")
        print(f"   Кол-во товаров: {category.product_list_str().count(chr(10)) + 1}")
        print(category.product_list_str())
        print()

    print(f"📊 Всего категорий: {Category.category_count}")
    print(f"📊 Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()

    # 🔽 Демонстрация функционала:
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    # 🛒 Проверка добавления товара
    print("\n🛒 До добавления:")
    print(category1.product_list_str())

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print("\n🛒 После добавления:")
    print(category1.product_list_str())
    print(f"Товаров в категории: {category1.product_list_str().count(chr(10)) + 1}")
    print(f"Общее кол-во товаров: {Category.product_count}")

    # ⭐ Проверка classmethod
    catalog = [product1]
    duplicate = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "Новая версия",
        "price": 200000.0,
        "quantity": 2,
    }
    updated_product = Product.new_product(duplicate, catalog)
    print(
        f"\n🆕 Обновлённый товар: {updated_product.name}, {updated_product.price}₽, {updated_product.quantity} шт."
    )

    # 💰 Проверка изменения цены
    print("\n💰 Установка новой корректной цены:")
    updated_product.price = 210000
    print(updated_product.price)

    print("\n💰 Понижение цены с подтверждением:")
    updated_product.price = 150000

    print(f"➡️ Текущая цена после понижения: {updated_product.price}")

    print("\n💰 Установка некорректной цены:")
    updated_product.price = -1
    updated_product.price = 0
