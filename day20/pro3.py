class Mobile:
    def __init__(self, brand, ram, processor, storage):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.storage = storage

    def display(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}, Processor: {self.processor}, Storage: {self.storage}")

mi = Mobile("Xiaomi", "6GB", "Snapdragon 720G", "128GB")



# print(mi)
# print(mi.brand)
samsung = Mobile("samsung", "512", "octacore", "1tb")
print(samsung.brand)