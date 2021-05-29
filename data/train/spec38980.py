import numpy as np 

def function(x):

	c4 = x
	m0 = 6
	paths = []
	try:
		if x > 1:
			c4 = c4*8
			m0 = 3*m0
			m0 = c4-m0
			paths.append(1)
		else:
			c4 = c4-m0
			c4 = c4-5
			c4 = 7-c4
			paths.append(2)
		if m0 <= 2:
			m0 = x/m0
			c4 = c4-9
			paths.append(3)
		else:
			x = 5+4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))