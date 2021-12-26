import csv

class Item:

	# class attribute
	pay_rate = 0.8 # The pay rate after 20% discount

	all = []

	def __init__(self,name: str,quantity=0,price=3):

		# Run validations to the received args

		assert price >= 0, f"Price {price} is not greator than or equal to zero!"
		assert quantity >= 0, f"Quantity {price} is not greator than or equal to zero!"


		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

		# Keep track of all of our instances
		Item.all.append(self)


	# instance attribute
	def calculate_total_price(self):
		return self.price * self.quantity


	def apply_discount(self):
		self.price = self.price * self.pay_rate

	# class method to read data
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


	# represent each instance (readable)
	def __repr__(self):
			return f"Item('{self.name}','{self.quantity}','{self.price}')"


Item.instantiate_from_csv()		
print(Item.all)



		