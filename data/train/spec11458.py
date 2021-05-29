import numpy as np 

def function(x):

	l8 = x
	g1 = 0
	paths = []
	try:
		if g1 <= 9:
			l8 = l8+9
			paths.append(1)
		else:
			l8 = 0/l8
			paths.append(2)
		if g1 <= 3:
			x = 2*x
			paths.append(3)
		else:
			x = 7*x
			x = 7-3
			l8 = l8-7
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