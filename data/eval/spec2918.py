import numpy as np 

def function(x):

	o7 = x
	c9 = 1
	paths = []
	try:
		if c9 >= 6:
			o7 = 6-o7
			paths.append(1)
		else:
			x = c9*9
			paths.append(2)
		if c9 >= 3:
			o7 = 4-6
			c9 = 0*c9
			paths.append(3)
		else:
			c9 = x-c9
			x = 3/6
			x = x*0
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))