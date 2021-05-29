import numpy as np 

def function(x):

	c4 = x
	b0 = x
	paths = []
	try:
		if x < 1:
			x = 8/c4
			paths.append(1)
		else:
			b0 = b0-0
			c4 = x/5
			x = 0*x
			paths.append(2)
		if c4 >= 4:
			c4 = c4-5
			paths.append(3)
		else:
			b0 = 5+b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))