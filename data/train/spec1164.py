import numpy as np 

def function(x):

	c7 = 7
	m4 = x
	paths = []
	try:
		if m4 > 4:
			c7 = 4+c7
			x = x+m4
			paths.append(1)
		else:
			m4 = 2*8
			paths.append(2)
		if c7 < 5:
			c7 = 8+c7
			c7 = x/6
			paths.append(3)
		else:
			c7 = c7+8
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