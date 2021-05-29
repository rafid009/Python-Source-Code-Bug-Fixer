import numpy as np 

def function(x):

	c0 = x
	m0 = 7
	paths = []
	try:
		if m0 >= 2:
			c0 = 1+x
			paths.append(1)
		else:
			c0 = 6-3
			paths.append(2)
		if m0 < 7:
			c0 = x+x
			m0 = 6*8
			c0 = 8*1
			paths.append(3)
		else:
			m0 = m0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))