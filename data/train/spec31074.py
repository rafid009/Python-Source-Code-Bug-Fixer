import numpy as np 

def function(x):

	g5 = x
	a8 = 6
	paths = []
	try:
		if x <= 1:
			g5 = g5*g5
			x = x-1
			paths.append(1)
		else:
			a8 = 9+4
			g5 = 8/g5
			x = g5-x
			paths.append(2)
		if g5 >= 1:
			x = g5-6
			g5 = 6-x
			paths.append(3)
		else:
			g5 = g5*9
			a8 = 5/5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))