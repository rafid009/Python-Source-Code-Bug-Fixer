import numpy as np 

def function(x):

	k1 = 7
	a3 = 7
	paths = []
	try:
		if x >= 7:
			a3 = 9-3
			paths.append(1)
		else:
			a3 = 1+x
			x = x+6
			paths.append(2)
		if k1 < 2:
			a3 = 6-k1
			x = 1-x
			a3 = a3-4
			paths.append(3)
		else:
			x = x/2
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