"""
public class Item{
    String itemName;
    double itemPrice;

    static String madeIn = "China"

    Item(String itemName,double itemPrice){
        this.itemName = itemName;
        this.itemPrice = itemPrice;
    }

}
"""

class Item:

    made_in = "China" # _ underscore means private access type
    _tariffs = "100%"

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price


    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

    @staticmethod
    def static_method():
        print(f"This is static method of Item")

    @classmethod
    def class_method(cls):
        print(f"This is  a class method: {cls.made_in}")


item1 = Item("Roman",100000)
item2 = Item("Book",2)
print(item1)
print(item2)

Item.class_method()

"""
Create Employee class:
        instance variables: employee_name, job_title, salary
        static variables: pay_tax
        
        instance methods:
            __init()__: declares and initializes all the instances variables
            __str()__: create string version of the object
            need to include
            work() method (display employee name + text "Working")
            
            class method:
            display_employee_tax_rate()
"""
