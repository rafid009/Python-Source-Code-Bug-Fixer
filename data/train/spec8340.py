import numpy as np 

def function(x):

	x4 = x
	g5 = x
	paths = []
	try:
		if g5 >= 0:
			x = x*g5
			x = 5/x
			paths.append(1)
		else:
			x4 = 7/x4
			paths.append(2)
		if g5 < 7:
			g5 = 3/7
			paths.append(3)
		else:
			x = x*x
			g5 = 5+x4
			g5 = 3/x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))