class Restaurant():

	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print("My restaurant's name is : "+self.name)
		print("My restaurant's type is : "+self.type)
		print("There are "+str(self.number_served)+" people eat lunch in my TRAIL")

	def open_restaurant(self):
		print("The restaurant:"+self.name+"is open")

	def increment(self,number):
		self.number_served+=number
"""
my_restaurant=Restaurant("Trail","Shanxi")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()			
my_restaurant.increment(20)
my_restaurant.describe_restaurant()
"""
class IceCreamStand(Restaurant):

	def __init__(self,ice_name,ice_type):
		super().__init__(ice_name,ice_type)
		self.flavors=["apple","banana","orange","strawbarry"]
	def show_kind(self):
		print("My shop's kinds are as following")
		#print(self.flavors)
		for kind in self.flavors:
			print('-'+kind)

my_ice=IceCreamStand("Trail_Ice","Sweet food")
my_ice.show_kind()