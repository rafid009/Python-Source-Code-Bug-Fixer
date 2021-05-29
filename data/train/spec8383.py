import numpy as np 

def function(x):

	b2 = 4
	c3 = 4
	paths = []
	try:
		if c3 < 5:
			b2 = x*b2
			paths.append(1)
		else:
			x = x/c3
			x = x+9
			x = x+5
			paths.append(2)
		if c3 <= 5:
			c3 = c3-8
			paths.append(3)
		else:
			c3 = 3*b2
			b2 = b2-4
			b2 = 1/b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		c3 = b2**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))