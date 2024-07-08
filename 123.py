import requests

# Получаем категории товаров
categories_url = "https://fakestoreapi.com/products/categories"
categories_response = requests.get(categories_url)
categories = categories_response.json()

# Выводим категории
print("Доступные категории товаров:")
for i, category in enumerate(categories, 1):
    print(f"{i}. {category}")

# Запрашиваем у пользователя выбор категории
choice = int(input("\nВведите номер категории, товары которой вы хотите просмотреть: ")) - 1
selected_category = categories[choice]

# Получаем товары выбранной категории
products_url = f"https://fakestoreapi.com/products/category/{selected_category}"
products_response = requests.get(products_url)
products = products_response.json()

# Выводим информацию о товарах
print(f"\nТовары в категории '{selected_category}':\n")
for product in products:
    print(f"Название: {product['title']}")
    print(f"Цена: ${product['price']}")
    print(f"Описание: {product['description']}")
    print(f"Рейтинг: {product['rating']['rate']} ({product['rating']['count']} оценок)")
    print("-" * 50)