import numpy as np 

def function(x):

	o6 = 2
	c8 = x
	paths = []
	try:
		if o6 >= 6:
			o6 = o6+9
			paths.append(1)
		else:
			x = 0-x
			x = x-o6
			paths.append(2)
		if x > 0:
			o6 = 0/x
			paths.append(3)
		else:
			o6 = 2+5
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