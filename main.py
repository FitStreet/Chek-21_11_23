"""Task 1"""

class CreateMixin:
    def create(self, key, todo):
        if key in self.todos:
            return 'Задача под таким ключом уже существует'
        else:
            self.todos[key] = todo
            return self.todos

class DeleteMixin:
    def delete(self, key):
        data = self.todos.pop(key)
        return f"удалили {data} задачу"

class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos

class ReadMixin():
    def read(self):
        sorted_todos = list(sorted(self.todos.items()))
        return sorted_todos


class ToDo(
    CreateMixin,
    UpdateMixin,
    DeleteMixin,
    ReadMixin
    ):
    todos = {}

    def set_deadline(self, deadline):
        import datetime
        time_ = datetime.datetime.now().strftime('%d/%m/%Y')
        deadline = deadline.split("/")
        time_ = time_.split('/') 
        deadline = list(map(int, deadline))
        time_ = list(map(int, time_)) 
        time_ = sum((time_[0], time_[1]*30, time_[2]*365))
        deadline = datetime.date(deadline[2], deadline[1], deadline[0])
        time_ = datetime.date.today() 
        return (deadline - time_).days


"""Task 2""" 

class Person:
    def __init__(self, name = None, last_name = None, age = None, email = None):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email  
    @property
    def name(self):
        return self.__name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def age(self):
        return self.__age
    @property
    def email(self):
        return self.__email  
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name
    @age.setter
    def age(self, new_age):
        self.__age = new_age
    @email.setter
    def email(self, new_email):
        self.__email = new_email

john = Person()
print(john.name) 
print(john.last_name) 
print(john.age) 
print(john.email) 
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) 
print(john.last_name) 
print(john.age) 
print(john.email) 

"""Task 3"""

class Dog:
    def voice(self):
        print("Гав")

class Cat:
    def voice(self):
        print("Мяу")

barsik = Cat()
rex = Dog()

def to_pet(pet):
    return pet.voice()

to_pet(barsik)
to_pet(rex)