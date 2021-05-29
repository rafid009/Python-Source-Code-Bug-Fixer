import numpy as np 

def function(x):

	m6 = 1
	c7 = 5
	paths = []
	try:
		if x <= 7:
			c7 = c7*5
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if c7 <= 6:
			m6 = m6+x
			c7 = c7-m6
			paths.append(3)
		else:
			c7 = 7-0
			c7 = 0+0
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