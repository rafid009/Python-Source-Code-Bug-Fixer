import numpy as np 

def function(x):

	g9 = x
	w0 = 1
	paths = []
	try:
		if g9 <= 8:
			w0 = g9/w0
			g9 = 5-g9
			w0 = w0/3
			paths.append(1)
		else:
			g9 = 5/7
			paths.append(2)
		if g9 > 8:
			g9 = 7-g9
			paths.append(3)
		else:
			w0 = w0+x
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