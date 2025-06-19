import os
import sys

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
        print(f"   Кол-во товаров: {len(category.products)}")
        for product in category.products:
            print(f"     - {product.name} ({product.price} ₽, {product.quantity} шт.)")
        print()

    print(f"📊 Всего категорий: {category.category_count}")
    print(f"📊 Всего товаров: {category.product_count}")


if __name__ == "__main__":
    main()
