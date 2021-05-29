import numpy as np 

def function(x):

	m3 = 4
	c6 = x
	paths = []
	try:
		if x <= 9:
			c6 = 0+c6
			c6 = c6/x
			paths.append(1)
		else:
			c6 = c6+7
			paths.append(2)
		if c6 <= 4:
			x = x+m3
			x = x-2
			paths.append(3)
		else:
			m3 = c6+x
			c6 = m3-7
			x = m3*x
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