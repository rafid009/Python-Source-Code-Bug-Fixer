import numpy as np 

def function(x):

	g3 = x
	a9 = x
	paths = []
	try:
		if a9 > 1:
			a9 = a9+0
			paths.append(1)
		else:
			g3 = 3-g3
			g3 = g3/7
			a9 = a9*5
			paths.append(2)
		if a9 >= 8:
			x = 4-2
			a9 = 8/1
			paths.append(3)
		else:
			x = x/2
			a9 = a9+a9
			x = g3-5
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