import numpy as np 

def function(x):

	g9 = x
	w0 = x
	paths = []
	try:
		if w0 < 9:
			x = 5*6
			g9 = 0+4
			g9 = 1/g9
			paths.append(1)
		else:
			w0 = 3*w0
			paths.append(2)
		if x < 9:
			w0 = 6+g9
			w0 = w0*x
			paths.append(3)
		else:
			g9 = w0/x
			g9 = 3-w0
			x = 4/x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		g9 = w0**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))