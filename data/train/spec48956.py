import numpy as np 

def function(x):

	u2 = x
	a4 = 4
	paths = []
	try:
		if a4 < 0:
			a4 = u2/a4
			paths.append(1)
		else:
			a4 = 2*a4
			paths.append(2)
		if u2 < 2:
			x = 4/x
			a4 = 1*6
			x = 4-x
			paths.append(3)
		else:
			x = 2/x
			x = 1/u2
			a4 = 4+a4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))