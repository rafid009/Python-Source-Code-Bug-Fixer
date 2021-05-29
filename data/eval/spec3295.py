import numpy as np 

def function(x):

	g7 = x
	k1 = 7
	paths = []
	try:
		if x > 8:
			k1 = k1+6
			k1 = k1*5
			x = 1-x
			paths.append(1)
		else:
			x = x-3
			x = x*x
			paths.append(2)
		if g7 < 8:
			x = x+1
			x = 3+2
			x = 1-x
			paths.append(3)
		else:
			g7 = 2-g7
			g7 = k1/k1
			k1 = k1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))