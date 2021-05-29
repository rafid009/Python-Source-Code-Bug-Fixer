import numpy as np 

def function(x):

	e5 = 0
	l0 = 1
	paths = []
	try:
		if x <= 4:
			e5 = e5+7
			e5 = 4/e5
			l0 = 9*l0
			paths.append(1)
		else:
			l0 = l0+7
			l0 = x-l0
			e5 = 4*e5
			paths.append(2)
		if l0 <= 4:
			e5 = 0-e5
			e5 = e5/l0
			l0 = x+4
			paths.append(3)
		else:
			l0 = e5*l0
			x = x+6
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