import numpy as np 

def function(x):

	c0 = 9
	m9 = 2
	paths = []
	try:
		if m9 >= 5:
			c0 = c0-x
			x = x/3
			paths.append(1)
		else:
			c0 = 7-c0
			m9 = m9-7
			m9 = c0/x
			paths.append(2)
		if m9 <= 7:
			x = x+x
			x = c0-1
			paths.append(3)
		else:
			c0 = 4-4
			m9 = 4/m9
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