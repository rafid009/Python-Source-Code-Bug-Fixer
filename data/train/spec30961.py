import numpy as np 

def function(x):

	c0 = x
	d9 = 7
	paths = []
	try:
		if d9 > 1:
			d9 = d9+6
			d9 = d9-5
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if d9 > 7:
			d9 = 4-d9
			paths.append(3)
		else:
			c0 = c0*0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))