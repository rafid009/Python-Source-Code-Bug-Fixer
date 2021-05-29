import numpy as np 

def function(x):

	c7 = 2
	o6 = 2
	paths = []
	try:
		if o6 > 6:
			x = x-x
			x = x-3
			paths.append(1)
		else:
			x = x+3
			c7 = 8-o6
			x = x+1
			paths.append(2)
		if x >= 6:
			c7 = c7-8
			x = c7*x
			o6 = 4-6
			paths.append(3)
		else:
			x = 7/c7
			x = x/c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))