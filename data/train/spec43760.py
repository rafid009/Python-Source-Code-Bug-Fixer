import numpy as np 

def function(x):

	m3 = 0
	c9 = 9
	paths = []
	try:
		if m3 <= 9:
			m3 = m3-4
			paths.append(1)
		else:
			c9 = c9/8
			m3 = c9+m3
			paths.append(2)
		if m3 >= 9:
			m3 = 0+c9
			m3 = x/m3
			paths.append(3)
		else:
			x = m3-x
			c9 = c9*9
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		c9 = m3**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))