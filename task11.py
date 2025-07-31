class Product:
    def get_delivery_method(self):
        pass

class PhysicalProduct(Product):
    def get_delivery_method(self):
        print("Yetkazib berish: kuryer orqali")

class DigitalProduct(Product):
    def get_delivery_method(self):
        print("Yuklab olish: elektron pochta yoki hisobdan")

product = PhysicalProduct()
product.get_delivery_method()

d_product = DigitalProduct()
d_product.get_delivery_method()

