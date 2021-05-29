import numpy as np 

def function(x):

	e2 = 5
	a6 = 3
	paths = []
	try:
		if x <= 8:
			x = e2*x
			paths.append(1)
		else:
			a6 = 2*6
			paths.append(2)
		if x >= 0:
			x = x*a6
			x = x/x
			x = x+8
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))