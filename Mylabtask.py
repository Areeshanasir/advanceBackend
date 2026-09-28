class person:
    def __init__(self, name):
        self.name = name
        
        def printname(self):
            print(self.name)
            
            p1=person("Tobias")
            p1=person("Linus")
            
            
            
            
            
            
    
            
            class book:
                library_name= "Campus Library"
                
                def __init__(self, title ):
                                          
                                           self.title = title 
                
                def mark_read(self):
                    self.is_read = True
                    print (Book.library_name)
                    print (Book("Done").library_name)
                    
                    
                class Dog:
                    
                          species = "Canine"   

    def __init__(self, name, age):
        self.name = name   
        self.age = age     

    def bark(self):        
        print(f"{self.name} says Woof!")

    def describe(self):    
        print(f"{self.name} is a {self.age}-year-old {self.species}")


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()       
dog2.describe()    

class Account:
    def _init_(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a = Account(1000)
a.deposit(500)
print(a.get_balance())


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"]

        return total

    def display_cart(self):
        print("Shopping Cart:")

        for item in self.items:
            print(item["name"], "-", item["price"])

        print("Total:", self.calculate_total())
                    
                    
                    
                    
                    
                    