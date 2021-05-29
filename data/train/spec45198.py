import numpy as np 

def function(x):

	a1 = 8
	l8 = x
	paths = []
	try:
		if l8 < 7:
			a1 = a1+3
			paths.append(1)
		else:
			x = 7-x
			a1 = 6+l8
			paths.append(2)
		if x <= 6:
			l8 = l8/l8
			a1 = 7+2
			paths.append(3)
		else:
			l8 = 2/l8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))