class Person:

    def __init__(self, name: str = "unknown", age: int = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{type(self).__name__}{self.__dict__}"


class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")
    # work()
    pass


class Tester(Employee):



    def work(self):
        print(f"{self.name} is testing the application")


class Developer(Employee):


    def work(self):
        print(f"{self.name} is developing the application")


employee1 = Tester("Roman",32,"SDET",100000)
employee2 = Developer("Liliya",30,"Dev",200000)

print(employee1)
print(employee2)

employee1.work()
