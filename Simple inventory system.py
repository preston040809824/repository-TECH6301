class Product
    def __init__(self, name, price, quantity, SKU):
            self.name=name
            self.price=price
            self.quantity=quantity
            self.SKU=SKU
            self.is_available=True

    def check_stock(self, name, SKU):
        for i in range(len(ls)):
            if (ls[i].name == name):
                return i
            if (ls[i].SKU == SKU):
                return i

    def purchase(self):
        name = input("Enter Product name: ")
        date = datetime.date.today()
        i = obj.check_stock(name)
        if i:
            ls[i].quantity += int(input("Enter quantity: "))
            ls[i].price = int(input("Enter product price: "))
            ls[i].date = date
        else:
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter product price: "))
            supplier = input("Enter Supplier: ")
            ob = Stock(name, price, supplier, quantity, date)
            ls.append(ob)


#name
#price
#quantity