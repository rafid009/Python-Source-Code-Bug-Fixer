import numpy as np 

def function(x):

	a6 = 1
	k4 = 3
	paths = []
	try:
		if a6 <= 7:
			a6 = 2*9
			a6 = 9*6
			a6 = 1/a6
			paths.append(1)
		else:
			k4 = k4*x
			k4 = 8*x
			k4 = 9*k4
			paths.append(2)
		if x > 1:
			x = 9+x
			k4 = 1/4
			paths.append(3)
		else:
			k4 = 2+k4
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