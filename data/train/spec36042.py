import numpy as np 

def function(x):

	o7 = 8
	c9 = x
	paths = []
	try:
		if o7 > 5:
			o7 = o7-c9
			x = x-9
			paths.append(1)
		else:
			x = 6+o7
			c9 = 0/c9
			c9 = c9-2
			paths.append(2)
		if o7 < 3:
			x = x/1
			c9 = x-c9
			x = x-x
			paths.append(3)
		else:
			c9 = c9-2
			o7 = o7+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))