import numpy as np 

def function(x):

	h5 = 4
	a9 = x
	paths = []
	try:
		if x >= 8:
			a9 = a9-3
			a9 = a9*a9
			a9 = 9-a9
			paths.append(1)
		else:
			x = 1+x
			a9 = a9+7
			h5 = h5*h5
			paths.append(2)
		if a9 < 6:
			h5 = 4/a9
			x = h5/7
			h5 = 5*x
			paths.append(3)
		else:
			a9 = 8*a9
			x = x-a9
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))