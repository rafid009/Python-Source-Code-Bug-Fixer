import numpy as np 

def function(x):

	j1 = x
	g0 = 7
	paths = []
	try:
		if g0 <= 0:
			g0 = 4-g0
			paths.append(1)
		else:
			g0 = 1/x
			g0 = x/j1
			paths.append(2)
		if g0 > 8:
			j1 = j1*j1
			g0 = g0-8
			paths.append(3)
		else:
			x = x+6
			j1 = 2*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))