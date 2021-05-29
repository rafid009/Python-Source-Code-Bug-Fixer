import numpy as np 

def function(x):

	a5 = x
	c2 = x
	paths = []
	try:
		if c2 < 6:
			c2 = 0+5
			a5 = a5+4
			paths.append(1)
		else:
			c2 = c2/a5
			x = 0+x
			paths.append(2)
		if c2 <= 9:
			a5 = 8*6
			c2 = 6-9
			paths.append(3)
		else:
			x = 4*2
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