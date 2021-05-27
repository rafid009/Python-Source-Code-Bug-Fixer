import numpy as np 

def function(x):

	c0 = x
	o9 = 1
	paths = []
	try:
		if c0 >= 3:
			c0 = 9*c0
			x = 5/o9
			paths.append(1)
		else:
			c0 = 1-c0
			paths.append(2)
		if o9 >= 7:
			c0 = 0/x
			x = o9-x
			x = x+8
			paths.append(3)
		else:
			c0 = 0-8
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		o9 = c0**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))