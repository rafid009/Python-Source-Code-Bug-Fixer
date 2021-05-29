import numpy as np 

def function(x):

	a0 = 9
	e4 = x
	paths = []
	try:
		if x <= 9:
			e4 = e4*x
			e4 = e4/7
			paths.append(1)
		else:
			a0 = 8/5
			paths.append(2)
		if a0 <= 9:
			e4 = e4+2
			paths.append(3)
		else:
			a0 = a0*6
			a0 = 8-2
			x = x/a0
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