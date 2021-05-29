import numpy as np 

def function(x):

	a5 = x
	g4 = 5
	paths = []
	try:
		if a5 < 0:
			a5 = 9*6
			g4 = 7-g4
			a5 = x+a5
			paths.append(1)
		else:
			a5 = a5-3
			paths.append(2)
		if g4 >= 5:
			g4 = 7/a5
			a5 = 0*a5
			a5 = a5+g4
			paths.append(3)
		else:
			a5 = a5+5
			a5 = x/g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))