import numpy as np 

def function(x):

	m8 = x
	c9 = x
	paths = []
	try:
		if m8 > 3:
			c9 = c9-m8
			paths.append(1)
		else:
			m8 = 3*x
			paths.append(2)
		if m8 < 6:
			x = 6+3
			paths.append(3)
		else:
			m8 = m8*c9
			c9 = c9+8
			c9 = c9-4
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))