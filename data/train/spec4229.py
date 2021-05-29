import numpy as np 

def function(x):

	g3 = x
	r2 = 1
	paths = []
	try:
		if r2 <= 3:
			g3 = 7-g3
			x = 8/x
			paths.append(1)
		else:
			r2 = r2-g3
			g3 = 0-r2
			x = r2-x
			paths.append(2)
		if g3 <= 8:
			g3 = 0-g3
			paths.append(3)
		else:
			r2 = 4-g3
			x = 6+3
			g3 = 1*g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))