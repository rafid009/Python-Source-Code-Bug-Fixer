import numpy as np 

def function(x):

	g6 = x
	f1 = 2
	x = 4
	paths = []
	try:
		if g6 <= 0:
			x = 1*x
			paths.append(1)
		else:
			f1 = 5*x
			paths.append(2)
		if g6 > 0:
			g6 = g6/6
			paths.append(3)
		else:
			g6 = 4*g6
			x = 8/5
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))