import numpy as np 

def function(x):

	l8 = x
	a0 = 5
	paths = []
	try:
		if l8 > 8:
			a0 = a0*7
			paths.append(1)
		else:
			a0 = 0-6
			l8 = 0-l8
			x = x+4
			paths.append(2)
		if l8 < 6:
			x = 3/x
			l8 = l8-5
			l8 = l8-5
			paths.append(3)
		else:
			a0 = a0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))