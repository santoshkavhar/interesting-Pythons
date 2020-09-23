# This practice code is from a Medium Blog
'''
#Class

class Pizza:

    #Class attribute:
    info = "This is a Pizza class!"
    
# Instantiate the class
obj = Pizza()

# Accessing the attribute:
print(obj.info)
'''

'''
# __init__

class Pizza:

	# Class attribute:
	info = "This is a Pizza class!"
	
	#instance attribute
	def __init__(self, type_):
		self.type_ = type_
	
# Instantiate the class
obj = Pizza(type_ = 'veggie')

# Accessing the attribute:
print("I want a", obj.type_ ,"pizza")
'''

'''
# __call__

class Pizza:

	# Class attribute
	info = "This is Pizza class"
	
	#instance attribute
	def __init__(self, type_):
		self.type_ = type_
		self.shape = 'round'
		
	# instance method:
	def __call__(self, shape = None):
		if shape:
			self.shape = shape
			return print("Submitting a", self.type_, "pizza order with a change of shape ----", self.shape)
		else:
			print("Submitting a", self.type_,"pizza order with default shape----",self.shape)
			
# Instantiate the class:
obj = Pizza(type_ = 'veggie')

# Calling the class:
obj('square')
obj()
'''

'''
# __repr__

class Pizza:

	# class Attribute:
	info = "This is a Pizza class"
	
	# instance attribute
	def __init__(self, type_):
		self.type_ = type_
		self.shape = 'round'
		
	# instance method
	def __repr__(self):
		tuple = "Type : "+ self.type_+", Shape: "+self.shape
		return tuple


# Instantiate the class:
obj = Pizza('veggie')

# Calling the class
print(obj)
'''		

'''		
# __str__

class Pizza:

	# Class attribute:
	info = "This is a Pizza class!"
	
	# instance attribute:
	def __init__(self, type_):
		self.type_ = type_
		self.shape = 'round'
		
	# instance method
	def __str__(self):
		tuple = "Type : "+ self.type_+", Shape: "+self.shape
		return tuple
		
# Instantiate the class
obj = Pizza(type_ = 'veggie')

# Print the class
print(obj)
'''

'''
# __dict__

class Pizza:

	# class attribute:
	info = "This is Pizza class!"
	
	# instance attribute:
	def __init__(self, type_, size):
		self.type_ = type_
		self.shape = 'round'
		self.size = size
		
		
# Instantiate the class:
obj = Pizza( 'veggie', 'small')

# Print the dict:
print(obj.__dict__)
'''

'''
# __dict__ modify

class Pizza:

	# class attribute:
	info = "This is a Pizza class!"
	
	# instance attribute:
	def __init__(self, type_, size):
		self.type_ = type_
		self.shape = 'round'
		self.size = size
		
# Instantiate the class:
obj = Pizza(type_ = 'veggie', size = 'small')

# change the size to medium
obj.__dict__['size'] = 'medium'

# Print the dict output:
print(obj.__dict__)
'''

'''
# __slot__

class Pizza:

	# class attribute:
	info = "This is a Pizza class!"
	
	# Defining slots:
	__slots__ = [ 'type_' , 'size', 'shape' ]
	
	# instance attribute:
	def __init__(self, type_, size):
		self.type_ = type_
		self.size = size
		self.shape = 'round'
		
# Instantiate the class:
obj = Pizza(type_ = 'veggie', size='small')
'''	

'''
# @staticmethod

class Pizza:
	
	# class attribute:
	info = "This is a Pizza class!"
	
	# Defining slots:
	__slots__ = ['type_','size','shape']
	
	# instance attribute:
	def __init__(self, type_, size):
		self.type_ = type_
		self.size = size
		self.shape = 'round'
		
	@staticmethod
	def get_veggie_ingredients():
		list_ingredients = ['onions','pepper','olives','jalapeneos','mushrooms']
		return list_ingredients
		
# Get the static method without initiating the class:
print(Pizza.get_veggie_ingredients() )
'''

'''
# @classmethod

class Pizza:

	# class attribute:
	info = "This is a Pizza class!"
	
	# Defining slots:
	__slots__ = ['type_','size','shape']
	
	# instance attribute:
	def __init__(self, type_, size):
		self.type_ = type_
		self.size = size
		self.shape = 'round'
		
	@staticmethod
	def get_veggie_ingredients():
		list_ingredients = ['onions','pepper','olives','jalapenoes','mushrooms']
		return list_ingredients
	
	@classmethod
	def determine_size(cls, type_, size):
		if size <= 14:
			return cls(type_, 'medium')
		else:
			return cla(type_, 'large')
	
# Instantiate the class:
obj = Pizza.determine_size(type_='veggie', size=12)
print(obj.type_ , "Pizza ordered of", obj.size, "and", obj.shape)
'''



