import numpy as np 

def function(x):

	g3 = x
	y8 = 5
	paths = []
	try:
		if g3 <= 1:
			g3 = g3/x
			g3 = 2+4
			g3 = g3*8
			paths.append(1)
		else:
			y8 = 5*5
			paths.append(2)
		if x < 5:
			y8 = y8/y8
			paths.append(3)
		else:
			g3 = g3+x
			g3 = 0/y8
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