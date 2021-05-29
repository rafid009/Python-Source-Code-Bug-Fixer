import numpy as np 

def function(x):

	m5 = x
	c6 = 8
	paths = []
	try:
		if c6 > 2:
			x = m5/8
			paths.append(1)
		else:
			x = x*2
			m5 = c6/4
			paths.append(2)
		if x < 0:
			c6 = 7+c6
			x = 2*x
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		c6 = m5**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))