import numpy as np 

def function(x):

	a8 = 8
	g3 = 5
	paths = []
	try:
		if x > 9:
			a8 = 1-7
			g3 = 8/5
			paths.append(1)
		else:
			g3 = g3*9
			a8 = a8-8
			paths.append(2)
		if g3 >= 0:
			x = 5-x
			a8 = a8-8
			g3 = g3*4
			paths.append(3)
		else:
			g3 = g3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))