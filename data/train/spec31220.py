import numpy as np 

def function(x):

	g6 = 4
	v9 = 8
	paths = []
	try:
		if x > 6:
			v9 = 3*v9
			x = 5+x
			paths.append(1)
		else:
			x = x*1
			g6 = 2*0
			x = x-8
			paths.append(2)
		if g6 <= 7:
			g6 = 4+g6
			v9 = 0*x
			paths.append(3)
		else:
			v9 = v9*7
			x = v9+x
			v9 = 4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))