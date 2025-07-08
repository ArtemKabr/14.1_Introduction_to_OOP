from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех товаров."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер с валидацией для цены товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input("Цена ниже. Подтвердить изменение? (y/n): ").lower()
            if confirm != "y":
                print("Изменение цены отменено.")
                return

        self.__price = new_price

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления товара."""
        pass

    @abstractmethod
    def __add__(self, other: object) -> int:
        """Абстрактный метод сложения количества товаров."""
        pass


class CreationLoggerMixin:
    """Миксин, выводящий в консоль информацию о создании объекта."""

    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"Создан объект {cls_name} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class Product(CreationLoggerMixin, BaseProduct):
    """Класс, описывающий товар."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Складывает количество товаров на складе, если они одного класса.
        Вызывает ошибку TypeError при попытке сложения объектов разных классов.
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.quantity + other.quantity

    @property
    def price(self) -> float:
        """
        Геттер для цены товара.
        :return: текущая цена
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Сеттер для цены. Проверяет, чтобы цена была положительной и подтверждает понижение.
        :param new_price: новое значение цены
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input("Цена ниже. Подтвердить изменение? (y/n): ").lower()
            if confirm != "y":
                print("Изменение цены отменено.")
                return

        self.__price = new_price

    @classmethod
    def new_product(
        cls, product_data: dict, existing_products: list["Product"]
    ) -> "Product":
        """
        Создаёт или обновляет товар. При совпадении названия — обновляет количество и цену.

        :param product_data: словарь с данными нового товара
        :param existing_products: список уже имеющихся товаров
        :return: экземпляр класса Product
        """
        for product in existing_products:
            if product.name == product_data["name"]:
                product.quantity += product_data["quantity"]
                if product_data["price"] > product.price:
                    product.price = product_data["price"]
                return product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


class Smartphone(Product):
    """
    Класс, описывающий смартфон.
    Наследуется от Product и добавляет характеристики смартфона.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс, описывающий газонную траву.
    Наследуется от Product и добавляет агрономические свойства.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс, описывает категорию товаров."""

    category_count = 0  # количество категорий
    product_count = 0  # общее количество всех товаров во всех категориях

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию, если это экземпляр Product или его наследников.
        Вызывает TypeError, если объект не является продуктом.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты и их наследников")
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории с общим количеством всех товаров.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        """
        Геттер для приватного списка продуктов.
        Возвращает строку с информацией о каждом продукте.
        """
        product_lines = [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        ]
        return "\n".join(product_lines)

    def product_list_str(self) -> str:
        """
        Возвращает строку с информацией о каждом товаре.
        """
        return "\n".join(str(product) for product in self.__products)
