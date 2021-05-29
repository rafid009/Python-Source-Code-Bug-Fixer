import numpy as np 

def function(x):

	l0 = x
	a8 = 6
	paths = []
	try:
		if l0 <= 3:
			a8 = 8*6
			paths.append(1)
		else:
			a8 = a8*l0
			x = 7-x
			paths.append(2)
		if l0 >= 1:
			x = 7*x
			x = 8-9
			l0 = l0-x
			paths.append(3)
		else:
			l0 = x*6
			l0 = l0+l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))