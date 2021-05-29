import numpy as np 

def function(x):

	c1 = 2
	o2 = x
	paths = []
	try:
		if o2 <= 3:
			c1 = 3*c1
			paths.append(1)
		else:
			o2 = 5+o2
			c1 = 2/c1
			paths.append(2)
		if o2 <= 2:
			o2 = 7*x
			o2 = 6/4
			o2 = x/3
			paths.append(3)
		else:
			o2 = 9+o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))