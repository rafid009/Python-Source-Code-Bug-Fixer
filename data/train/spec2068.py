import numpy as np 

def function(x):

	c3 = x
	m4 = x
	paths = []
	try:
		if c3 > 4:
			x = 1+7
			m4 = 8*6
			paths.append(1)
		else:
			m4 = 2/m4
			paths.append(2)
		if c3 < 4:
			m4 = 1-m4
			paths.append(3)
		else:
			c3 = 0-c3
			c3 = c3-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))