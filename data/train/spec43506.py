import numpy as np 

def function(x):

	m7 = 8
	c4 = x
	paths = []
	try:
		if m7 < 8:
			c4 = c4+m7
			x = 3-1
			paths.append(1)
		else:
			x = m7+c4
			c4 = 0*c4
			c4 = c4+m7
			paths.append(2)
		if c4 > 5:
			m7 = 2-c4
			m7 = m7/2
			paths.append(3)
		else:
			m7 = 5*5
			c4 = 9*c4
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		c4 = m7**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))