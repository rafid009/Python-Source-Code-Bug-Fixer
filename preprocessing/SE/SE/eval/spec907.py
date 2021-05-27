import numpy as np 

def function(x):

	w2 = 5
	g8 = x
	paths = []
	try:
		if w2 > 8:
			w2 = w2*g8
			paths.append(1)
		else:
			w2 = w2+4
			w2 = w2-w2
			g8 = g8/5
			paths.append(2)
		if g8 >= 5:
			x = w2/x
			x = x-x
			paths.append(3)
		else:
			x = x-3
			x = w2*g8
			x = 4-g8
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