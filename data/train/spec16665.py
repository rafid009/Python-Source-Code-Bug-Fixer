import numpy as np 

def function(x):

	c8 = 4
	m4 = x
	paths = []
	try:
		if x <= 3:
			m4 = m4+3
			m4 = m4+4
			paths.append(1)
		else:
			m4 = m4-7
			x = 7+m4
			c8 = 4-1
			paths.append(2)
		if x >= 6:
			x = x*4
			paths.append(3)
		else:
			c8 = c8+c8
			c8 = 5-c8
			m4 = m4-6
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))