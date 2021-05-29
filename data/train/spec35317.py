import numpy as np 

def function(x):

	c0 = x
	m2 = x
	paths = []
	try:
		if c0 > 7:
			c0 = c0/5
			m2 = m2*x
			x = x-5
			paths.append(1)
		else:
			c0 = c0-c0
			m2 = m2-9
			m2 = x-8
			paths.append(2)
		if m2 > 2:
			x = 6-3
			c0 = m2/x
			x = x*9
			paths.append(3)
		else:
			x = 6+x
			c0 = c0*9
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