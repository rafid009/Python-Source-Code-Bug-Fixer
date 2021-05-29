import numpy as np 

def function(x):

	m6 = x
	c9 = 6
	x = 7
	paths = []
	try:
		if c9 <= 5:
			x = 5+6
			m6 = m6-4
			paths.append(1)
		else:
			x = c9-x
			m6 = 5+m6
			paths.append(2)
		if c9 >= 5:
			m6 = m6*x
			m6 = 5-m6
			m6 = 1/m6
			paths.append(3)
		else:
			x = m6-9
			c9 = 4/c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))