class Car:
    def __init__(self , brand , name):
        self.brand = brand
        self.name = name
    
    def fullName(self):
        return f"fullName is : {self.brand } , {self.name}"


class ElectricCar(Car):
    def __init__(self, brand, name , batterySize):
        self.batterySize  = batterySize
        super().__init__(brand, name)         



tesla = ElectricCar("Tesla","model s","89kwh")
print(tesla.fullName())