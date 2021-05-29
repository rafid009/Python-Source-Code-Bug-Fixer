import numpy as np 

def function(x):

	w9 = x
	g1 = 2
	paths = []
	try:
		if w9 >= 2:
			w9 = w9*4
			paths.append(1)
		else:
			x = w9*x
			x = 6-x
			g1 = g1*6
			paths.append(2)
		if g1 <= 4:
			x = x+x
			g1 = x+5
			g1 = g1/x
			paths.append(3)
		else:
			g1 = x*g1
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