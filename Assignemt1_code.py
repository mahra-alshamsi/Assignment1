#Order class
class Order:
    """A Class to represent an order. """
    def __init__(self, order_number, delivery_address, delivery_date, delivery_method, order_status):
        #Initializing Order class attributes
        self.__order_number = order_number
        self.__delivery_address = delivery_address
        self.__delivery_date = delivery_date
        self.__delivery_method = delivery_method
        self.__order_status = order_status
        self.__items = []

#Setter Getter methods for order class attributes
    def set_order_number(self, order_number):
        self.__order_number = order_number
    def get_order_number(self):
        return self.__order_number

    def set_delivery_address(self, delivery_address):
        self.__delivery_address = delivery_address
    def get_delivery_address(self):
        return self.__delivery_address

    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date
    def get_delivery_date(self):
        return self.__delivery_date

    def set_delivery_method(self, delivery_method):
        self.__delivery_method = delivery_method
    def get_delivery_method(self):
        return self.__delivery_method

    def set_order_status(self, order_status):
        self.__order_status = order_status
    def get_order_status(self):
        return self.__order_status

#Function for customers to add items in their order
    def add_item(self, item):
        self.__items.append(item)
#Function to add total price of the order
    def calculate_total_price(self):
        total_price = sum(items.get_total_items_price() for items in self.__items)
        return total_price

#Item class
class Item:
    """A Class to represent an item."""
    def __init__(self, item_code, item_description, item_quantity, item_price):
        #Initializing Item class attributes
        self.__item_code = item_code
        self.__item_description = item_description
        self.__item_quantity = item_quantity
        self.__item_price = item_price
        self.__total_items_price = 0

#Setter getter method for item attributes
    def set_item_code(self, item_code):
        self.__item_code = item_code
    def get_item_code(self):
        return self.__item_code

    def set_item_description(self, item_description):
        self.__item_description = item_description
    def get_item_description(self):
        return self.__item_description

    def set_item_quantity(self, item_quantity):
        self.__item_quantity = item_quantity
    def get_item_quantity(self):
        return self.__item_quantity

    def set_item_price(self, item_price):
        self.__item_price = item_price
    def get_item_price(self):
        return self.__item_price

# Function to calculate and set the total price for an item
    def set_total_items_price(self):
        self.__total_items_price = self.__item_quantity * self.__item_price
    def get_total_items_price(self):
        return self.__total_items_price

#Customer class
class Customer:
    """A Class to represent a customer."""
    def __init__(self, customer_name, customer_contact_info, customer_delivery_address):
        #Initializing Customer class attributes
        self.__customer_name = customer_name
        self.__customer_contact_info = customer_contact_info
        self.__customer_delivery_address = customer_delivery_address

    # Setter getter method for Customer attributes
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name
    def get_customer_name(self):
        return self.__customer_name

    def set_customer_contact_info(self, customer_contact_info):
        self.__customer_contact_info = customer_contact_info
    def get_customer_contact_info(self):
        return self.__customer_contact_info

    def set_customer_delivery_address(self, customer_delivery_address):
        self.__customer_delivery_address = customer_delivery_address
    def get_customer_delivery_address(self):
        return self.__customer_delivery_address

#Delivery note class
class DeliveryNote:
    """A class to represent a delivery note."""
    def __init__(self, order_number, recipient_name, delivery_date):
        #Initializing delivery note attributes
        self.__order_number = order_number
        self.__recipient_name = recipient_name
        self.__delivery_date = delivery_date
        self.__items = []
        self.__total_items_price = 0
        self.__taxes_fees = 0

#Setter getter methods for delivery note attributes
    def set_order_number(self, order_number):
        self.__order_number = order_number
    def get_order_number(self):
        return self.__order_number

    def set_recipient_name(self, recipient_name):
        self.__recipient_name = recipient_name
    def get_recipient_name(self):
        return self.__recipient_name

    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date
    def get_delivery_date(self):
        return self.__delivery_date

    def set_items(self, items):
        self.__items = items
    def get_items(self):
        return self.__items

    def set_total_items_price(self, total_items_price):
        self.__total_items_price = total_items_price
    def get_total_items_price(self):
        return self.__total_items_price

    def set_taxes_fees(self, taxes_fees):
        self.__taxes_fees = taxes_fees
    def get_taxes_fees(self):
        return self.__taxes_fees

    #Generate and display the delivery note
    def generate_delivery_note(self):
        #Function to calculate the total price with taxes and fees
        self.__total_items_price = sum(item.get_item_quantity() * item.get_total_items_price() for item in self.__items)
        self.__taxes = self.__total_items_price * 0.05 #5% tax is applied
        print("\n--- Delivery Note ---")
        print(f"Order Number: {self.__order_number}")
        print(f"Recipient name: {self.__recipient_name.get_customer_name()}")
        print(f"Delivery Date: {self.__delivery_date}")
        print(f"Delivery Address: {self.__recipient_name.get_customer_delivery_address()}")
        print("\nItems Delivered:")
        for item in self.__items:
            print(f"Item Code: {item.get_item_code()}, Description: {item.get_item_description()}, "
                  f"Quantity: {item.get_item_quantity()}, Unit Price: {item.get_item_price()}, "
                  f"Total Price: {item.get_total_items_price()}")
        print(f"\nSubtotal: AED {self.__total_items_price}")
        print(f"Taxes and Fees: AED {self.__taxes}")
        print(f"Total Charges: AED {self.__total_items_price + self.__taxes}")

#Customer information
customer1 = Customer("Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")

#Order items
item1 = Item("ITM001", "Wireless Keyboard", 1, 100.00)
item2 = Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00)
item3 = Item("ITM003", "Laptop Cooling Pad", 1, 120.00)
item4 = Item("ITM004", "Camera Lock", 3, 15.00)

#Set total price for each item
item1.set_total_items_price()
item2.set_total_items_price()
item3.set_total_items_price()
item4.set_total_items_price()

#Create order and add items
order1 = Order("DEL123456789", "45 Knowledge Avenue, Dubai, UAE", "2025-01-25", "Courier", "Pending")
order1.add_item(item1)
order1.add_item(item2)
order1.add_item(item3)
order1.add_item(item4)

#Create delivery note and associate with order and customer
delivery_note1 = DeliveryNote(order1.get_order_number(), customer1, "2025-01-25")
delivery_note1.set_items([item1, item2, item3, item4])

#Generate and display delivery note
delivery_note1.generate_delivery_note()




