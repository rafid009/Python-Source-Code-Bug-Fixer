import numpy as np 

def function(x):

	c4 = 4
	d4 = x
	paths = []
	try:
		if d4 < 5:
			d4 = 9+d4
			d4 = d4+1
			x = x/4
			paths.append(1)
		else:
			x = x+d4
			x = 1*x
			d4 = c4/d4
			paths.append(2)
		if c4 >= 1:
			x = x*7
			paths.append(3)
		else:
			x = 6*6
			x = x-5
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		c4 = d4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))