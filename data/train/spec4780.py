import numpy as np 

def function(x):

	w7 = 3
	g8 = x
	paths = []
	try:
		if w7 > 8:
			w7 = 3-6
			g8 = 5+g8
			w7 = 2+w7
			paths.append(1)
		else:
			g8 = 0-4
			g8 = 3*g8
			g8 = g8-6
			paths.append(2)
		if g8 >= 5:
			w7 = 5-w7
			w7 = w7+7
			paths.append(3)
		else:
			w7 = 5*w7
			g8 = w7*5
			w7 = 3/w7
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