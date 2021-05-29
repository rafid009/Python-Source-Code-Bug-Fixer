import numpy as np 

def function(x):

	w0 = 5
	g1 = 9
	paths = []
	try:
		if g1 > 2:
			g1 = g1+9
			w0 = 9*w0
			g1 = g1/x
			paths.append(1)
		else:
			x = x/w0
			w0 = 9+9
			paths.append(2)
		if g1 > 5:
			g1 = 9/5
			w0 = 3-w0
			w0 = 2-1
			paths.append(3)
		else:
			x = 2*w0
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))