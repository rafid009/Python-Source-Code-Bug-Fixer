import numpy as np 

def function(x):

	l8 = x
	m9 = x
	paths = []
	try:
		if x < 7:
			l8 = 7-m9
			x = x+8
			m9 = m9+4
			paths.append(1)
		else:
			l8 = l8+8
			paths.append(2)
		if x >= 6:
			l8 = m9-7
			l8 = 8-l8
			l8 = 7*l8
			paths.append(3)
		else:
			l8 = 3-4
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