import numpy as np 

def function(x):

	c6 = x
	m5 = x
	paths = []
	try:
		if x <= 2:
			m5 = 6+x
			c6 = c6-c6
			x = 1-m5
			paths.append(1)
		else:
			c6 = 9+c6
			c6 = c6+c6
			x = 5/x
			paths.append(2)
		if c6 <= 5:
			m5 = m5+c6
			c6 = c6+x
			paths.append(3)
		else:
			x = x-9
			c6 = c6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))