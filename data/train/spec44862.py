import numpy as np 

def function(x):

	x9 = x
	a1 = 5
	paths = []
	try:
		if a1 < 2:
			a1 = x/2
			a1 = a1+4
			x = x9*x
			paths.append(1)
		else:
			x9 = 3-0
			paths.append(2)
		if x9 < 7:
			a1 = 5-1
			a1 = x/a1
			x9 = 7-x9
			paths.append(3)
		else:
			x9 = x9-x9
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))