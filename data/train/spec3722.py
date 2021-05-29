import numpy as np 

def function(x):

	g6 = 7
	a5 = 9
	paths = []
	try:
		if x >= 7:
			g6 = g6*1
			paths.append(1)
		else:
			x = 7*x
			g6 = g6-8
			x = a5/x
			paths.append(2)
		if x < 9:
			a5 = a5*x
			paths.append(3)
		else:
			x = 7+5
			x = x+x
			g6 = g6*a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		g6 = a5**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))