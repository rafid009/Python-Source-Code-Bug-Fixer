import numpy as np 

def function(x):

	g6 = x
	x6 = 2
	paths = []
	try:
		if x > 5:
			x6 = x6-x
			x6 = x6-1
			paths.append(1)
		else:
			x6 = x*g6
			x6 = 7/x6
			g6 = x6*g6
			paths.append(2)
		if x6 < 5:
			x = 5*x
			paths.append(3)
		else:
			g6 = g6-2
			g6 = 9+1
			x6 = x6+x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))