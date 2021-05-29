import numpy as np 

def function(x):

	c8 = 8
	b2 = 1
	paths = []
	try:
		if c8 < 8:
			x = x+c8
			paths.append(1)
		else:
			x = 0/b2
			x = 1-4
			c8 = c8/6
			paths.append(2)
		if b2 > 0:
			b2 = b2+3
			c8 = c8/c8
			paths.append(3)
		else:
			x = x*6
			c8 = b2-c8
			x = 2*x
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