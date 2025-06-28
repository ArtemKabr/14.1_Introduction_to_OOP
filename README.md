

# 📘 14.1–14.2 Введение в ООП (E-commerce Core)

Проект реализует базовые сущности интернет-магазина с использованием ООП на Python.  
Задания направлены на закрепление навыков работы с:
- классами и объектами,
- инкапсуляцией (приватные атрибуты, геттеры/сеттеры),
- методами классов (`@classmethod`),
- тестированием и инструментами статической проверки.

---
## Структура проекта

├── src/
│   ├── __init__.py
│   ├── models.py           # Классы Product и Category
│   └── utils.py            # Загрузка данных из JSON
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Фикстуры для тестов
│   ├── test_models.py      # Тесты для Product и Category
│   └── test_utils.py       # Тесты для функции загрузки
│
├── .coverage
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── main.py                 # Демонстрация работы классов
├── poetry.lock
├── products.json           # Исходные данные
├── pyproject.toml
├── pytest.ini
└── README.md


## 🚀 Функциональность

- `Product` — класс товара:
    - приватная цена (`__price`)
  - геттер `price` и сеттер с валидацией
  - подтверждение при понижении цены через `input()`
  - метод `@classmethod new_product()` — создание из словаря с учётом дубликатов
  - магические методы:
    - `__str__` — формат: `Название, X руб. Остаток: X шт.`
    - `__add__` — сумма стоимости товаров (price × quantity)

- **Category** — класс категории:
  - приватный список `__products`
  - метод `add_product()` — добавляет товар и обновляет счётчик
  - `products` — геттер (возвращает список объектов `Product`)
  - `product_list_str()` — строка с товарами для вывода
  - `__str__` — формат: `Категория, количество продуктов: X шт.`

- Подсчёт товаров и категорий через атрибуты класса (`product_count`, `category_count`)
- Загрузка данных из `products.json` через `load_data_from_json`

- ✅ **100% покрытие тестами** (`pytest + pytest-cov`)
- - 97% покрытие кода тестами (`pytest + pytest-cov`)
- Используются:
  - `monkeypatch` — для `input()`
  - `capsys` — для проверки вывода
  - фикстуры из `conftest.py``

- 👨‍🔧 Интеграция с `pre-commit`:
  - `flake8` — стиль кода (PEP8)
  - `black` — автоформатирование
  - `isort` — сортировка импортов
  - `mypy` — статическая проверка типов (опционально)

---

## 🧰 Установка и запуск

1. Клонируйте репозиторий и установите зависимости:

```bash
git clone https://github.com/ArtemKabr/14.1_Introduction_to_OOP.git
cd 14.1_Introduction_to_OOP
poetry install


## 🧰 Установка и запуск

1. Клонируйте репозиторий и установите зависимости:

```bash
git clone https://github.com/ArtemKabr/14.1_Introduction_to_OOP.git
cd 14.1_Introduction_to_OOP
poetry install

2. Установите хуки pre-commit:

pre-commit install
pre-commit run --all-file

3. Запуск main.py:

python main.py

4. **Тесты**

pytest

5. Для проверки покрытия:

pytest --cov=src.models --cov-report=term-missing
6. Для HTML-отчёта:

pytest --cov=src.models --cov-report=html
start htmlcov/index.html
