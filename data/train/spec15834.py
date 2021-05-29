import numpy as np 

def function(x):

	x5 = x
	g3 = 9
	paths = []
	try:
		if x5 < 8:
			g3 = g3-9
			paths.append(1)
		else:
			x = x+x
			x5 = x5+4
			x = x/x
			paths.append(2)
		if g3 <= 8:
			x = x+x5
			g3 = x5/4
			paths.append(3)
		else:
			g3 = 0-g3
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