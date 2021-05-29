import numpy as np 

def function(x):

	d9 = x
	c7 = 2
	paths = []
	try:
		if d9 < 1:
			x = x/4
			x = x/5
			x = 4-0
			paths.append(1)
		else:
			c7 = d9*c7
			d9 = d9+x
			d9 = d9+x
			paths.append(2)
		if d9 <= 9:
			d9 = d9/c7
			c7 = 4*c7
			x = 5+x
			paths.append(3)
		else:
			c7 = 5+c7
			x = x/2
			x = x-5
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		c7 = d9**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))