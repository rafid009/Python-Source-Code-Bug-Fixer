import numpy as np 

def function(x):

	m4 = 0
	c8 = 8
	paths = []
	try:
		if m4 >= 8:
			x = x-7
			m4 = m4*9
			paths.append(1)
		else:
			c8 = 5+8
			paths.append(2)
		if m4 < 2:
			m4 = m4+4
			x = 7/x
			m4 = 8-m4
			paths.append(3)
		else:
			m4 = 6*m4
			c8 = c8-c8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))