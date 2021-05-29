import numpy as np 

def function(x):

	c0 = 4
	m7 = 1
	paths = []
	try:
		if c0 <= 6:
			c0 = 2-x
			paths.append(1)
		else:
			c0 = c0-2
			x = 4-x
			paths.append(2)
		if m7 > 1:
			m7 = m7/9
			m7 = 7/x
			paths.append(3)
		else:
			c0 = 4+c0
			c0 = m7+x
			x = x*m7
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