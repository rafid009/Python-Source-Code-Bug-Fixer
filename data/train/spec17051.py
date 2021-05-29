import numpy as np 

def function(x):

	m6 = x
	c7 = x
	paths = []
	try:
		if c7 >= 4:
			x = x-m6
			m6 = m6-3
			paths.append(1)
		else:
			c7 = c7*3
			x = 6*x
			m6 = 3*m6
			paths.append(2)
		if x < 6:
			c7 = c7+3
			c7 = 8*c7
			x = 0+c7
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))