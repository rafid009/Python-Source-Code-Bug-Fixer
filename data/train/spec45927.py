import numpy as np 

def function(x):

	m4 = 3
	u0 = 5
	paths = []
	try:
		if x > 6:
			u0 = u0+2
			u0 = 5-u0
			paths.append(1)
		else:
			u0 = u0+2
			paths.append(2)
		if u0 >= 8:
			m4 = 8-1
			u0 = 7/u0
			u0 = 9*u0
			paths.append(3)
		else:
			x = 8/x
			m4 = m4-x
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