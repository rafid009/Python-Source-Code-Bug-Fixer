import numpy as np 

def function(x):

	c3 = 3
	m2 = x
	paths = []
	try:
		if m2 >= 2:
			x = 8-5
			x = 5+2
			paths.append(1)
		else:
			c3 = c3-7
			paths.append(2)
		if c3 <= 3:
			x = m2/c3
			m2 = 8-x
			paths.append(3)
		else:
			m2 = m2/1
			c3 = c3+m2
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))