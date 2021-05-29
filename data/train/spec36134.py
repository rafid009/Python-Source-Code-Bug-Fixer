import numpy as np 

def function(x):

	c4 = 1
	m8 = x
	paths = []
	try:
		if c4 <= 8:
			m8 = m8-c4
			paths.append(1)
		else:
			c4 = c4*5
			paths.append(2)
		if x <= 6:
			c4 = c4/c4
			m8 = 2-4
			m8 = 3-x
			paths.append(3)
		else:
			x = c4-x
			m8 = m8+0
			m8 = 4-m8
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