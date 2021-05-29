import numpy as np 

def function(x):

	g6 = 6
	r2 = 2
	paths = []
	try:
		if g6 < 2:
			x = 7-x
			paths.append(1)
		else:
			x = x/3
			r2 = 2-6
			paths.append(2)
		if g6 <= 7:
			g6 = 0+x
			r2 = 2+r2
			paths.append(3)
		else:
			r2 = 7-7
			g6 = 1-x
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