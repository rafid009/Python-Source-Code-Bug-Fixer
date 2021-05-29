import numpy as np 

def function(x):

	m1 = 9
	c7 = x
	paths = []
	try:
		if m1 >= 6:
			c7 = c7/c7
			c7 = c7-c7
			paths.append(1)
		else:
			m1 = 5-5
			paths.append(2)
		if m1 < 1:
			c7 = c7+5
			paths.append(3)
		else:
			x = x-9
			x = x-c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))