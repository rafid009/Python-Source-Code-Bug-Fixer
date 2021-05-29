import numpy as np 

def function(x):

	c2 = 9
	m2 = 4
	paths = []
	try:
		if c2 > 8:
			m2 = m2-3
			m2 = m2/7
			paths.append(1)
		else:
			m2 = m2-5
			c2 = c2-7
			paths.append(2)
		if c2 <= 5:
			m2 = m2-m2
			paths.append(3)
		else:
			x = x+c2
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