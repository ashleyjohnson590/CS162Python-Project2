# Author: Ashley Johnson
# Date: 4/1/2021
# Description: StoreTester.py contains unit testers for store.py.
import unittest
from Store import Store
from Store import Product
from Store import Customer
from Store import InvalidCheckoutError


class test_store(unittest.TestCase):

    def testStore(self):
        myBanana = Product(1, "banana", "this is a yellow fruit", 1.00, 5)
        myApple = Product(2, "apple", "this is a red fruit", 2.00, 6)
        myPear = Product(3, "pear", "this is a banana pear", 6.00, 1)
        customer1 = Customer(123, "Ashley", False)
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
        product_title = myStore.lookup_product_from_id(99)
        foundID = myStore.product_search("banana")
        self.assertListEqual([1,3],foundID)

        myStore.add_product_to_member_cart(1, 123)
        myStore.add_product_to_member_cart(2, 123)
        myStore.add_product_to_member_cart(3, 456)
        myStore.add_product_to_member_cart(3, 123)
        name = myStore.lookup_member_from_id(123)
        self.assertEqual("Ashley", name)
        name = myStore.lookup_member_from_id(999)
        self.assertIsNone(name)
        price = 0
        try:
            price = myStore.check_out_member(123)
        except InvalidCheckoutError:
            print("caught error")

    def sameCustomer(self):
        myCustomer = Customer(123, "Ashley", True)
        try:
            myStore.add_member(myCustomer)
        except:
            print("failed as expected")

    def testProduct(self):
        newProduct = Product(421, "cheese", "moldy milk", 3.00, 24)
        productTitle = newProduct.get_title()
        self.assertEqual(productTitle, "cheese")
    def testCustomer(self):
        myCustomer = Customer(10, "chelsea", False)
        myProduct = Product(324, "ice cream", "delicious desert", 10.00, 53)
        myCustomer.add_product_to_cart(324)
        myName = myCustomer.get_name()
        self.assertEqual(myName, "chelsea")
        myID = myCustomer.get_customer_id()
        self.assertEqual(myID, 10)
        P2 = Product(693, "mac and cheese", "hot snack", 20.00, 67)
        myCustomer.add_product_to_cart(693)
        myCustomer.add_product_to_cart(693)
        myCustomer.empty_cart()
        myCart = myCustomer.get_cart()
        self.assertEqual(len(myCart),0)

if __name__ == '__main__':
    unittest.main(exit=False)
