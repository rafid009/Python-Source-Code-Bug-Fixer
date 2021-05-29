import numpy as np 

def function(x):

	m4 = 8
	e7 = 6
	paths = []
	try:
		if m4 >= 1:
			m4 = 7+e7
			paths.append(1)
		else:
			x = 5/x
			x = 1+x
			x = x-x
			paths.append(2)
		if x < 3:
			x = x-2
			m4 = m4*x
			paths.append(3)
		else:
			e7 = 2*e7
			e7 = 7/e7
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