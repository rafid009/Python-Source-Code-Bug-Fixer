import numpy as np 

def function(x):

	m4 = x
	c1 = x
	paths = []
	try:
		if c1 > 2:
			c1 = c1-9
			c1 = 8+m4
			c1 = m4/5
			paths.append(1)
		else:
			x = 2-x
			m4 = 4+8
			paths.append(2)
		if c1 < 6:
			c1 = 9+c1
			c1 = c1+5
			paths.append(3)
		else:
			m4 = m4/6
			x = 6-9
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