import numpy as np 

def function(x):

	w8 = x
	g3 = 5
	paths = []
	try:
		if w8 <= 2:
			x = 0/x
			g3 = 2+g3
			paths.append(1)
		else:
			w8 = w8*x
			paths.append(2)
		if w8 > 3:
			g3 = g3*6
			x = 3-g3
			w8 = w8*4
			paths.append(3)
		else:
			x = x*x
			x = 8+x
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