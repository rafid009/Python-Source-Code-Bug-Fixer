import numpy as np 

def function(x):

	g6 = 8
	a7 = 5
	x = x
	paths = []
	try:
		if g6 <= 8:
			g6 = g6+8
			x = 6+x
			a7 = 7+2
			paths.append(1)
		else:
			a7 = x*9
			a7 = a7-4
			x = 5+0
			paths.append(2)
		if x > 6:
			g6 = g6*x
			paths.append(3)
		else:
			x = 7*x
			g6 = 7/7
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