import numpy as np 

def function(x):

	g3 = x
	g5 = x
	x = x
	paths = []
	try:
		if g3 < 7:
			g3 = x/g3
			g5 = g5+g5
			g5 = g5-3
			paths.append(1)
		else:
			x = g5-g5
			g3 = g3/2
			paths.append(2)
		if x > 4:
			g5 = 9+g5
			g5 = g5-3
			paths.append(3)
		else:
			x = g5*x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g3 = g5**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))