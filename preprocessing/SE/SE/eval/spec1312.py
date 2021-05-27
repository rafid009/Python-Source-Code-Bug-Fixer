import numpy as np 

def function(x):

	c0 = x
	m8 = 8
	paths = []
	try:
		if m8 < 9:
			c0 = 2-c0
			paths.append(1)
		else:
			c0 = c0-c0
			paths.append(2)
		if x <= 9:
			c0 = c0/5
			c0 = c0*7
			m8 = m8-6
			paths.append(3)
		else:
			x = 7-x
			m8 = 7+m8
			m8 = x+1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))