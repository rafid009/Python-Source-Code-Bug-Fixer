import numpy as np 

def function(x):

	b2 = x
	c3 = x
	paths = []
	try:
		if c3 > 0:
			x = 1*2
			c3 = c3+7
			paths.append(1)
		else:
			c3 = c3/x
			b2 = b2+0
			paths.append(2)
		if b2 <= 6:
			x = 8+7
			paths.append(3)
		else:
			b2 = b2-9
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