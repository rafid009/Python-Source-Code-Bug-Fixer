import numpy as np 

def function(x):

	r2 = 3
	g7 = x
	paths = []
	try:
		if x >= 2:
			r2 = r2-r2
			paths.append(1)
		else:
			x = g7+x
			x = r2-6
			x = 1-0
			paths.append(2)
		if g7 <= 1:
			r2 = 8*g7
			r2 = 3*r2
			g7 = 9-g7
			paths.append(3)
		else:
			x = 1/3
			r2 = 9+r2
			r2 = r2+6
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))