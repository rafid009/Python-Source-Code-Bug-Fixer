import numpy as np 

def function(x):

	a6 = 7
	i9 = 3
	paths = []
	try:
		if a6 < 5:
			a6 = 3/a6
			i9 = 7*x
			paths.append(1)
		else:
			a6 = a6/4
			a6 = a6/i9
			paths.append(2)
		if x > 3:
			i9 = 3/i9
			paths.append(3)
		else:
			i9 = a6+i9
			i9 = 9+i9
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