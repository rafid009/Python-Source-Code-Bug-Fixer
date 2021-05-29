import numpy as np 

def function(x):

	g8 = 2
	w9 = x
	paths = []
	try:
		if g8 <= 6:
			x = 9-x
			paths.append(1)
		else:
			w9 = x+w9
			paths.append(2)
		if g8 <= 7:
			w9 = w9/g8
			w9 = w9-w9
			x = 4*x
			paths.append(3)
		else:
			x = x-g8
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