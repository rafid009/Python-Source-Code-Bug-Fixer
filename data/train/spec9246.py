import numpy as np 

def function(x):

	w4 = 8
	g3 = 6
	paths = []
	try:
		if x >= 7:
			g3 = g3+0
			x = 9*w4
			paths.append(1)
		else:
			g3 = g3+w4
			w4 = w4-7
			g3 = 4*g3
			paths.append(2)
		if g3 <= 1:
			g3 = g3*2
			g3 = 6+4
			g3 = 1*5
			paths.append(3)
		else:
			g3 = 7/4
			g3 = 5+g3
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