import numpy as np 

def function(x):

	v9 = x
	c4 = 5
	paths = []
	try:
		if x <= 8:
			v9 = 9-v9
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if v9 < 7:
			x = x-c4
			c4 = 6-1
			c4 = c4+4
			paths.append(3)
		else:
			c4 = c4-8
			x = x*2
			v9 = v9+v9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))