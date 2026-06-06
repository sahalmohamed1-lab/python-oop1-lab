#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("Size must be Small, Medium or Large")
    
    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1

size = input("Enter coffee size(Small, Medium or Large): ")
price = float(input("Enter coffee price: "))

coffee = Coffee(size, price)

print(f"Size: {coffee.size}")
print(f"Price: {coffee.price}")

coffee.tip()

print(f"New price: {coffee.price}")
        