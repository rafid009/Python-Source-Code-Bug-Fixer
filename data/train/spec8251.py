import numpy as np 

def function(x):

	m4 = x
	c7 = 5
	paths = []
	try:
		if c7 < 2:
			x = x*x
			m4 = x*9
			x = 0-x
			paths.append(1)
		else:
			m4 = m4+m4
			m4 = m4/6
			paths.append(2)
		if x >= 6:
			x = m4-x
			c7 = c7-9
			x = x-m4
			paths.append(3)
		else:
			c7 = c7+5
			x = x+5
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