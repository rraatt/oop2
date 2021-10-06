class Product:
    __slots__ = ['name', 'price']

    def __init__(self, name, price):
        if isinstance(name, str) and isinstance(price, int or float):
            # Check for correct input.
            self.name = name
            self.price = price
        else:
            raise TypeError("Incorrect info for new product!")

    def __str__(self):
        return f'{self.name} {self.price}'


class Customer:
    __slots__ = ['name', 'surname', 'mobile']

    def __init__(self, name, surname, mobile):
        self.name = name
        self.surname = surname
        self.mobile = mobile

    def __str__(self):
        return f'{self.name} {self.surname} {self.mobile}'


class Order:
    def __init__(self, customer):
        if isinstance(customer, Customer):
            # Check if the input is correct class object
            self.info = customer.__str__()
            # Save info about customer.
            self.prod_list = []
            self.total = 0
        else:
            raise TypeError("Argument for order should be Customer type!")

    def add_item(self, product):
        if isinstance(product, Product):
            # Add an item to item list and ad up to order total
            self.prod_list.append(product.name)
            self.total += product.price
        else:
            raise TypeError("Argument for new item should be Product type!")

    def checkout(self):
        return f'total for the order: {self.total} Items bought: {self.prod_list} Customer info: {self.info}'


John = Customer('John', 'Smith', '0123456789')
Prod1 = Product('Cheese', 5)
Prod2 = Product('Bread', 3)

Ord = Order(John)
Ord.add_item(Prod1)
Ord.add_item(Prod2)
print(Ord.checkout())
