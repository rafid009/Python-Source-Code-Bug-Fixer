import numpy as np 

def function(x):

	w7 = 6
	g1 = x
	paths = []
	try:
		if g1 > 2:
			x = x*7
			x = 4+x
			w7 = g1-g1
			paths.append(1)
		else:
			w7 = w7/x
			paths.append(2)
		if w7 <= 4:
			x = x+4
			w7 = 9+5
			w7 = 6*g1
			paths.append(3)
		else:
			g1 = x-x
			x = x/3
			w7 = 2+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))