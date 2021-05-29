import numpy as np 

def function(x):

	g1 = 3
	e7 = x
	paths = []
	try:
		if x < 5:
			x = x/9
			g1 = g1*3
			g1 = 8/g1
			paths.append(1)
		else:
			g1 = 9/g1
			g1 = x/e7
			x = 4/x
			paths.append(2)
		if g1 >= 4:
			e7 = e7+0
			paths.append(3)
		else:
			e7 = 5/e7
			e7 = e7+e7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))