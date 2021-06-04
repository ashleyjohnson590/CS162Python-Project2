#Author: Ashley Johnson
#Date: 4/1/2021
#Description: Program is a store simulator with 3 private classes: product
# customer, and store. Classes keep track of store inventory, a list
# of customers, and whether the customer is a premium member.Program
# keeps track of store inventory and customer purchases and charges.Program
#keeps track of customer purchases. Premium members are not charged for
#shipping.

class InvalidCheckoutError(Exception):
    pass
class Product:
    """class initializes 5 private data members: the store's product ID, name of product, product
    description, price and quantity available."""
    def __init__(self, product_id, title, description, price, quantity_available):
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """gets ID of product."""
        return self._product_id

    def get_title(self):
        """gets name of product."""
        return self._title

    def get_description(self):
        """gets description of product."""
        return self._description

    def get_price(self):
        """gets the product price."""
        return self._price

    def get_quantity_available(self):
        """ gets the quantity available of the product."""
        return self._quantity_available

    def decrease_quantity(self):
        """ decreases the quanitity available by 1."""
        self._quantity_available -= 1
        print("quantity now {}".format(self._quantity_available))

class Customer:
    """class initializes 3 private data members: customer name, ID, premiumMember."""
    def __init__(self, customer_id, name, premium_member):
        self._customer_id = customer_id
        self._name = name
        self._premium_member = premium_member
        self._cart = []


    def get_name(self):
        """gets the customer Name."""
        return self._name

    def get_customer_id(self):
        """"gets the customer ID."""
        return self._customer_id

    def get_cart(self):
        """gets list of customer products."""
        return self._cart

    def is_premium_member(self):
        """returns whether the customer is a premium member(true) or not(false)."""
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """adds a customer product to customer cart."""
        self._cart.append(product_id)

    def empty_cart(self):
        """empties the customer cart"""
        self._cart=[]

class Store:
    """class initializes 2 private data members: number of products in store inventory, and number of customers
    as members."""
    _inventory = {}
    _membership = {}

    def __init__(self, inventory, membership):
        self._inventory = inventory
        self._membership = membership

    def add_product(self, product):
        """gets a product object and adds it to inventory."""
        self._inventory.append(product)

    def add_member(self, member):
        """gets a customer object and adds it to membership."""
        """makes sure member ID doesn't exist."""
        member_num = member.get_customer_id()
        try:
            self._membership[member_num]
        except KeyError:
            self._membership[member_num]=member
            print("Added member number {}".format(member_num))
        except:
            message="This member ID already exists. Please give different member ID."
            print(message)


    def lookup_product_from_id(self, product_id):
        """gets a product ID and returns the product title."""
        inventory = self._get_inventory()
        try:
            myProduct = inventory[product_id]
        except KeyError:
            eMsg = "product ID not found: {}".format(product_id)
            print(eMsg)
        except:
            title = myProduct.get_title()
            return title

    def get_product_from_id(self, product_id):
        """gets a product ID and returns the product."""
        inventory = self._get_inventory()
        print(inventory)
        myProduct = None
        try:
            myProduct = inventory[product_id]
        except KeyError:
            eMsg = "product ID not found: {}".format(product_id)
            print(eMsg)
        return myProduct
    def lookup_member_from_id(self, customer_id):
        """gets and returns customer name from ID."""
        myCustomers = self._get_customers()
        name = None
        try:
            customerFound = myCustomers[customer_id]
            name = customerFound.get_name()
        except KeyError:
            print("customer ID not found")
        return name



    def _get_inventory(self):
        """gets a list of products available."""
        return self._inventory
    def _get_customers(self):
        return self._membership
    def product_search(self, search_string):
        """takes a string to search and returns a list of ID codes for all inventory products
         that has a matching description."""
        myInventory = self._get_inventory()
        foundID = []
        for key in myInventory:
            myProduct = myInventory[key]
            title = myProduct.get_title()
            myDescription = myProduct.get_description()
            print(title)
            if search_string.lower() in title.lower() or search_string.lower() in myDescription.lower():
                foundID.append(key)
        return foundID

    def add_product_to_member_cart(self, product_id, customer_id):
        """gets a product ID and a customer ID. If both are found and product is available, product is
        added to cart"""
        myInventory= self._get_inventory()

        try:
            thisProduct = myInventory[product_id]
            print(product_id)
        except KeyError:
            eMsg = "product ID not found: {}".format(product_id)
            print(eMsg)


        myCustomers = self._get_customers()
        myInventory = self._get_inventory()
        thisCustomer = None
        thisProduct = None
        try:
            thisCustomer = myCustomers[customer_id]
        except KeyError:
            customerError = "customer ID not found: {}".format(customer_id)
            print(customerError)
            return
        try:
            thisProduct = myInventory[product_id]
        except KeyError:
            Error = "product ID not found: {}".format(product_id)
            print(Error)
            return
        thisCustomer.add_product_to_cart(product_id)
                #customer = myCustomers[customer_id]

    def check_out_member(self, customer_id):
        """gets a customer ID and returns the charge for that member's cart. Charge includes all items in cart plus
        shipping cost."""
        myCustomers = self._get_customers()
        thisCustomer = None
        try:
            thisCustomer = myCustomers[customer_id]
        except KeyError:
            customerError = "customer ID not found: {}".format(customer_id)
            print(customerError)
            raise InvalidCheckoutError()
        name = thisCustomer.get_name()
        is_premium = thisCustomer.is_premium_member()
        customerCart = thisCustomer.get_cart()
        print("customer cart: {}".format(customerCart))

        total = 0
        for product in customerCart:

            thisProduct = self.get_product_from_id(product)
            if thisProduct:
                quantity_available = thisProduct.get_quantity_available()
                if quantity_available > 0:
                    price=thisProduct.get_price()
                    total += price
                    print("price is now {}.".format(total))
                    thisProduct.decrease_quantity()
                else:
                    message = "sorry we are out of {}."
                    name = thisProduct.get_title()
                    print(message.format(name))
            else:
                eMsg = "product ID not found in store: {}"
                print(eMsg.format(product))
        if not thisCustomer.is_premium_member():
            shippingcosts = .07*total
            print("shipping costs is {}.".format(shippingcosts))
            total += shippingcosts
            print("total costs is {}".format(total))
        else:
            print("congrats you are a premium member, no shipping costs.")
        thisCustomer.empty_cart()
        """figure out if i need to add shipping. if not premium message not premium add 7%."""
        return total

def main(customer_id):
    myBanana = Product(1, "banana", "this is a yellow fruit", 1.00, 5)
    myApple = Product(2, "apple", "this is a red fruit", 2.20, 6)
    myPear = Product(3, "pear", "this is a pear", 3.35, 10)
    customer1 = Customer(123, "Ashley", True)
    customer2 = Customer(456, "brandon", False)
    myProducts = {
        1: myBanana,
        2: myApple,
        3: myPear
    }
    myCustomers = {
        123: customer1,
        456: customer2
    }
    myStore = Store(myProducts, myCustomers)
    myStore.add_product_to_member_cart(1, 123)
    myStore.add_product_to_member_cart(2, 456)
    myStore.add_product_to_member_cart(3, 456)
    myStore.add_product_to_member_cart(3, 123)
    try:
        return myStore.check_out_member(customer_id)
    except InvalidCheckoutError:
        print("invalid check out.")


if __name__ == '__main__':

    total = main(456)
    print("your cost is {} ".format(total))