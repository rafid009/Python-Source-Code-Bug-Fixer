import numpy as np 

def function(x):

	x5 = 1
	g1 = 1
	x = 6
	paths = []
	try:
		if g1 <= 1:
			x5 = x-g1
			paths.append(1)
		else:
			x5 = x5+7
			paths.append(2)
		if g1 <= 2:
			x5 = 2-x5
			g1 = 4+6
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))