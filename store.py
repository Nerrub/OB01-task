class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self,item_name, price):
        self.items[item_name] = price
    def delite_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
    def get_price(self, item_name):
        return self.items.get(item_name)
    def upgrade_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

#создадим магазины
store1 = Store("Продуктовый магазин", "Ленина 1")
store2 = Store("Магазин электроники", "Трухинова 6а")
store3 = Store("Концелярский магазин", "переулок Здоровья 10")

#добавим товары

store1.add_item("Яблоки","60 ")
store1.add_item("Батон","30 ")
store1.add_item("Сок","120 ")
store2.add_item("Калькулятор","900 ")
store2.add_item("Телевизор","23000 ")
store2.add_item("Ноутбук","94000 ")
store3.add_item("Бумага а4","800 ")
store3.add_item("Блокнот","130 ")
store3.add_item("Фламастеры","315 ")

#использование методов
store3.add_item("Карандаши","150")
print(store3.items)

store3.delite_item("Блокнот")
print(store3.items)


print("Стоимость фламастеров:",store3.get_price("Фламастеры"))

store3.upgrade_price("Бумага а4","900")
print(store3.items)