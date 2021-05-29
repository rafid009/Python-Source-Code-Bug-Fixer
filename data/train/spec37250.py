import numpy as np 

def function(x):

	o4 = x
	c9 = x
	x = 1
	paths = []
	try:
		if c9 >= 1:
			c9 = 7*c9
			x = c9/9
			o4 = 1+9
			paths.append(1)
		else:
			x = 2-1
			c9 = 9/c9
			paths.append(2)
		if x <= 3:
			x = c9/2
			o4 = 2+o4
			paths.append(3)
		else:
			o4 = o4+4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))