import numpy as np 

def function(x):

	a5 = 4
	g4 = x
	paths = []
	try:
		if g4 <= 8:
			a5 = 9+a5
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if a5 < 2:
			x = x*g4
			paths.append(3)
		else:
			g4 = x+g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))