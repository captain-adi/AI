class Vehicle:
    def __init__(self, brand, wheel):
        self.brand = brand
        self.wheel = wheel

    def show(self):
        print(f"a proper vehicles with {self.wheel} wheels and the name of the brand is {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, wheel , color):
         super().__init__(brand,wheel)
         self.color = color
    def show(self):
        print(f"car with Color : {self.color}  and have {self.wheel} ,which are made by {self.brand}")
  

obj = Car(brand="TATA" , wheel=4 ,  color="red"  )
obj.show()