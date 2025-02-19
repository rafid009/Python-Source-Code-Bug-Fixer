import numpy as np 

def function(x):

	g8 = x
	w1 = x
	paths = []
	try:
		if g8 < 1:
			g8 = 8*g8
			g8 = g8/5
			paths.append(1)
		else:
			g8 = w1*g8
			g8 = 5/g8
			paths.append(2)
		if g8 >= 8:
			w1 = w1+6
			paths.append(3)
		else:
			w1 = w1*w1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))