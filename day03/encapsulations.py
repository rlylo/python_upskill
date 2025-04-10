import numbers


class Item:

    def __init__(self,item_name: str = "unknown",item_price: numbers = 0):
        self.__item_name = None #private
        self.__item_price = None #private
        self.set_item_name(item_name)
        self.set_item_price(item_price)


    def get_item_name(self) -> str:
        return self.__item_name

    def get_item_price(self) -> numbers:
        return self.__item_price

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_item_price(self, item_price: numbers):
        if item_price <0:
            raise RuntimeError(f"Item price can't be negative or zero: {item_price}")
        self.__item_price = item_price

    def __str__(self):
        return f"{self.__dict__}"


item1 = Item()
item1.set_item_name("Pen")
print(item1)
item1.set_item_price(5)
print(item1)
print(item1.get_item_name())

item2 = Item("Laptop",1000)
print(item2)