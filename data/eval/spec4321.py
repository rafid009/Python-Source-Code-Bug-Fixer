import numpy as np 

def function(x):

	d5 = 0
	c0 = 9
	paths = []
	try:
		if x >= 0:
			x = 4-x
			c0 = d5-4
			c0 = d5*c0
			paths.append(1)
		else:
			c0 = 4-c0
			c0 = 0+c0
			paths.append(2)
		if c0 <= 9:
			x = 3*x
			x = x+9
			d5 = c0+8
			paths.append(3)
		else:
			x = 1-x
			d5 = 5+d5
			c0 = 6*c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))