import numpy as np 

def function(x):

	m3 = x
	c7 = x
	paths = []
	try:
		if c7 < 0:
			m3 = m3+4
			c7 = c7-c7
			paths.append(1)
		else:
			m3 = m3*0
			c7 = x*4
			x = 0*x
			paths.append(2)
		if x < 2:
			m3 = m3-8
			x = 2+x
			paths.append(3)
		else:
			x = x-4
			c7 = 9+3
			m3 = m3-7
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