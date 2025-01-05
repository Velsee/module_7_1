class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products()
        existing_products_dict = {}

        # Формируем словарь существующих товаров
        if existing_products:
            for product in existing_products.split('\n'):
                name, weight, category = product.split(', ')
                existing_products_dict[(name, category)] = float(weight)

        # Обработка новых продуктов
        for product in products:
            key = (product.name, product.category)
            if key in existing_products_dict:
                # Увеличиваем вес существующего продукта
                existing_products_dict[key] += product.weight
                print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_products_dict[key]}.")
            else:
                # Записываем новый продукт
                existing_products_dict[key] = product.weight

        # Записываем все товары в файл
        with open(self.__file_name, 'w') as file:
            for (name, category), weight in existing_products_dict.items():
                file.write(f"{name}, {weight}, {category}\n")

# Пример использования классов:

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
