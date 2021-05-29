import numpy as np 

def function(x):

	c3 = x
	o7 = 6
	paths = []
	try:
		if x > 3:
			c3 = 3*3
			c3 = 1/5
			x = 7-x
			paths.append(1)
		else:
			o7 = o7-9
			paths.append(2)
		if x > 7:
			x = x/8
			c3 = c3*3
			paths.append(3)
		else:
			c3 = 3+c3
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