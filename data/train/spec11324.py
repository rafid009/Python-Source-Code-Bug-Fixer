import numpy as np 

def function(x):

	c9 = 5
	b3 = x
	paths = []
	try:
		if c9 > 1:
			c9 = 0*c9
			paths.append(1)
		else:
			x = 7-x
			x = x+c9
			b3 = b3/b3
			paths.append(2)
		if c9 < 7:
			x = 8-x
			x = x-9
			paths.append(3)
		else:
			x = 2/x
			b3 = x*c9
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))