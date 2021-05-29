import numpy as np 

def function(x):

	p9 = 7
	c9 = x
	x = x
	paths = []
	try:
		if x < 9:
			c9 = c9+9
			c9 = p9*c9
			paths.append(1)
		else:
			c9 = 9-1
			p9 = p9+x
			x = 2+x
			paths.append(2)
		if c9 <= 7:
			p9 = p9+x
			paths.append(3)
		else:
			x = 9/x
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