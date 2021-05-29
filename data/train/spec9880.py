import numpy as np 

def function(x):

	c0 = x
	d0 = 7
	paths = []
	try:
		if x < 4:
			d0 = 7*d0
			x = x+7
			paths.append(1)
		else:
			x = 1+5
			paths.append(2)
		if x >= 7:
			c0 = c0-3
			d0 = 4-c0
			paths.append(3)
		else:
			x = 7/d0
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