import numpy as np 

def function(x):

	c0 = x
	m8 = 6
	paths = []
	try:
		if m8 > 6:
			c0 = m8-c0
			c0 = c0/c0
			c0 = c0*7
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if m8 > 2:
			c0 = 1-c0
			x = 5+x
			paths.append(3)
		else:
			m8 = m8/4
			m8 = m8-6
			m8 = 0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))