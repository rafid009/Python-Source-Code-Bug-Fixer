import numpy as np 

def function(x):

	a9 = 6
	g0 = 9
	paths = []
	try:
		if a9 < 8:
			x = x+a9
			paths.append(1)
		else:
			x = x/a9
			paths.append(2)
		if g0 >= 4:
			a9 = a9-g0
			paths.append(3)
		else:
			g0 = g0/x
			a9 = x-g0
			a9 = a9*a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		g0 = a9**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))