class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=10

	def get_descriptive_name(self):
		long_name=str(self.year)+' '+self.make+' '+self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")

	def update_odometer(self,mileage):
		"""
		禁止里程表读数回调
		"""
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!")
		self.odometer_reading=mileage

	def increment_odometer(self,miles):
		self.odometer_reading+=miles

	def fill_gas_tank(self):
		print('fighting!')
"""
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2000)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
"""
class Battery():
	"""电动车的电瓶"""
	def __init__(self,battery_size=70):
		self.battery_size=battery_size

	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-kWh battery")

	def get_range(self):
		if self.battery_size==70:
			range=240
		elif self.battery_size==85:
			range=270
		message="This car can go approximately "+str(range)
		message+=" miles on a full charge."
		print(message)
class ElectricCar(Car):
	#电动汽车的独到之处
	def __init__(self,make, model,year):
		"""初始化父类属性"""
		super().__init__(make,model,year)
		self.battery=Battery() #类中使用另一个类
