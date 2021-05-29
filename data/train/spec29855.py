import numpy as np 

def function(x):

	b2 = 0
	c8 = 5
	paths = []
	try:
		if c8 < 6:
			x = x-b2
			b2 = b2/4
			paths.append(1)
		else:
			c8 = 6*c8
			paths.append(2)
		if b2 < 3:
			c8 = c8*c8
			paths.append(3)
		else:
			b2 = b2+6
			c8 = b2/5
			c8 = 9/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))