class Product:
    """Класс, представляющий товар."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, представляющий категорию товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
