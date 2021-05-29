import numpy as np 

def function(x):

	g8 = 1
	a1 = x
	paths = []
	try:
		if a1 < 8:
			g8 = g8-a1
			a1 = 1+a1
			x = x/g8
			paths.append(1)
		else:
			a1 = 3-a1
			g8 = g8-g8
			a1 = 3*7
			paths.append(2)
		if a1 >= 8:
			x = x*x
			paths.append(3)
		else:
			a1 = 0/7
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))