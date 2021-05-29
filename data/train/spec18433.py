import numpy as np 

def function(x):

	m5 = 3
	c7 = 9
	paths = []
	try:
		if c7 >= 9:
			c7 = c7/4
			m5 = x-m5
			paths.append(1)
		else:
			m5 = 8-4
			paths.append(2)
		if m5 >= 1:
			c7 = 8-m5
			paths.append(3)
		else:
			c7 = 3/4
			x = m5*m5
			m5 = 8/m5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))