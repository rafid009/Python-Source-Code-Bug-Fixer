import numpy as np 

def function(x):

	m5 = 2
	c0 = x
	paths = []
	try:
		if x >= 3:
			x = x+x
			x = c0*1
			c0 = 3*2
			paths.append(1)
		else:
			c0 = c0-7
			m5 = m5/4
			paths.append(2)
		if m5 > 3:
			c0 = c0/c0
			paths.append(3)
		else:
			m5 = m5*8
			c0 = m5+c0
			m5 = m5*7
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