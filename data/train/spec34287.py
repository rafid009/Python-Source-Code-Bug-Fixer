import numpy as np 

def function(x):

	c7 = x
	m8 = 2
	x = 3
	paths = []
	try:
		if c7 > 4:
			m8 = m8*8
			c7 = c7/9
			paths.append(1)
		else:
			c7 = 3/m8
			c7 = 5*5
			x = x-m8
			paths.append(2)
		if c7 < 6:
			c7 = x-6
			x = c7-x
			paths.append(3)
		else:
			c7 = 8-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))