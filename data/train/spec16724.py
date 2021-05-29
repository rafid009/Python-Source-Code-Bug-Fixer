import numpy as np 

def function(x):

	w4 = 6
	g9 = 9
	paths = []
	try:
		if g9 >= 1:
			w4 = 6/w4
			g9 = x/2
			paths.append(1)
		else:
			w4 = w4/w4
			paths.append(2)
		if w4 < 0:
			w4 = w4/5
			g9 = g9*0
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))