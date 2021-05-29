import numpy as np 

def function(x):

	o5 = x
	c6 = x
	paths = []
	try:
		if o5 >= 2:
			o5 = 6-c6
			paths.append(1)
		else:
			o5 = o5*x
			paths.append(2)
		if c6 <= 6:
			c6 = x-c6
			paths.append(3)
		else:
			c6 = c6-4
			c6 = 0*c6
			o5 = o5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))