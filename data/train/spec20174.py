import numpy as np 

def function(x):

	c7 = x
	o6 = 2
	paths = []
	try:
		if o6 >= 1:
			c7 = 5+2
			c7 = 8*6
			o6 = c7*7
			paths.append(1)
		else:
			o6 = 5-9
			paths.append(2)
		if c7 > 1:
			c7 = x/3
			o6 = 4+4
			c7 = 2*c7
			paths.append(3)
		else:
			x = 6*o6
			x = x-4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		o6 = c7**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))