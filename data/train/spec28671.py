import numpy as np 

def function(x):

	w2 = 3
	g0 = x
	x = x
	paths = []
	try:
		if w2 > 5:
			g0 = g0*6
			w2 = w2+7
			w2 = w2+0
			paths.append(1)
		else:
			x = x-w2
			g0 = 8+g0
			w2 = w2-w2
			paths.append(2)
		if x < 5:
			x = g0*g0
			x = x/x
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))