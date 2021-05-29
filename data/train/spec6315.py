import numpy as np 

def function(x):

	a6 = 3
	v1 = x
	paths = []
	try:
		if x < 9:
			v1 = v1*7
			x = a6-5
			x = 3*x
			paths.append(1)
		else:
			a6 = a6*1
			x = x/x
			paths.append(2)
		if a6 < 6:
			a6 = 9+4
			paths.append(3)
		else:
			v1 = 1+3
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