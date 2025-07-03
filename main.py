import os
import sys

from src.models import Category, LawnGrass, Product, Smartphone
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

    # 📱 Создание смартфонов
    smartphone1 = Smartphone("iPhone 15", "512GB", 210000, 4, 97.5, "15", 512, "Gray")
    smartphone2 = Smartphone(
        "Samsung S23", "256GB", 190000, 3, 96.2, "S23", 256, "Black"
    )

    # 🌿 Создание газонной травы
    grass1 = LawnGrass(
        "Газонная трава", "Элитная", 500, 10, "Россия", "5 дней", "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2", "Для тени", 450, 5, "США", "7 дней", "Темно-зеленый"
    )

    # ✅ Сложение однотипных
    print("\n✅ Сложение смартфонов:")
    print(smartphone1 + smartphone2)

    print("\n✅ Сложение трав:")
    print(grass1 + grass2)

    # ❌ Ошибка при сложении разных типов
    print("\n❌ Попытка сложить смартфон и траву:")
    try:
        result = smartphone1 + grass1
    except TypeError as e:
        print(f"Ошибка: {e}")

    # ✅ Проверка ограничения на добавление продукта
    category_smartphones = Category("Смартфоны", "Категория", [])
    category_smartphones.add_product(smartphone1)

    # ❌ Попытка добавить строку вместо товара
    print("\n❌ Попытка добавить не-продукт в категорию:")
    try:
        category_smartphones.add_product("не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")
