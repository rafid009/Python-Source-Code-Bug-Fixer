import numpy as np 

def function(x):

	v4 = 8
	g7 = x
	paths = []
	try:
		if v4 <= 2:
			x = 0*2
			paths.append(1)
		else:
			v4 = v4-v4
			g7 = g7*2
			x = x+8
			paths.append(2)
		if x > 6:
			v4 = v4-x
			x = 3/x
			v4 = 3+9
			paths.append(3)
		else:
			v4 = 4-8
			g7 = g7/g7
			v4 = 8*v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))