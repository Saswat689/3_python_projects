# OOP Principles
# Here are some things I learnt n this project.

# Encapsulation - 	Prevent user from accessing certain attributes.
# Abstraction - Abstract(hide) the information that is unnecessary by using single _ before methods.
# Inheritance - Inherit attributes from a parent class.
# Polymorphism - A single entity that knows how to handle different objects.eg len() func in python.

import csv

# parent class
class Item:

	# class attribute
	pay_rate = 0.8 # The pay rate after 20% discount

	all = []

	def __init__(self,name: str,quantity=0,price=3):

		# Run validations to the received args

		assert price >= 0, f"{self.__class__.__name__} {price} is not greator than or equal to zero!"
		assert quantity >= 0, f"Quantity {price} is not greator than or equal to zero!"


		# Assign to self object

		self.__name = name
		self.price = price
		self.quantity = quantity

		# Keep track of all of our instances
		Item.all.append(self)

	# Property Decorator = Read Only Attribute	
	@property
	def name(self):
		return self.__name
		

	#allow users to set new values to attributes
	@name.setter
	def name(self,value):
		self.__name = value	

	# instance attribute
	def calculate_total_price(self):
		return self.price * self.quantity


	def apply_discount(self):
		self.price = self.price * self.pay_rate


	# class methods send class as a parameter
	@classmethod

	# instantiate the class via the data inside files(good practise)
	def instantiate_from_csv(cls):
		with open('items.csv','r') as f:
			# Covert csv file to a dictionary
			reader = csv.DictReader(f)
			# convert dictionary to a list
			items = list(reader)

		for item in items:
			Item(
				name=item.get('name'),
				price=float(item.get('price')),
				quantity=int(item.get('quantity'))
			)


	@staticmethod	
	# static method doesn't receive anything	
	def is_integer(num):
		if isinstance(num,float):
			return num.is_integer()
		elif isinstance(num,int):
			return True	
		else:
			return False	


	# represent each instance (readable)
	def __repr__(self):
			return f"Item('{self.name}','{self.quantity}','{self.price}')"
			

# child class
class Phone(Item):

	def __init__(self,name: str,quantity=0,price=3,broken_phones=0):
		# Call to super function to have access to all attributes/methods from the parent class
		super().__init__(
			name,price,quantity
		)

		# Run validations to the received args

		assert broken_phones >= 0, f"Quantity {broken_phones} is not greator than or equal to zero!"


		# Assign to self object
		self.broken_phones = broken_phones



		
