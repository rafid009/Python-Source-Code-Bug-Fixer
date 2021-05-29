import numpy as np 

def function(x):

	g4 = x
	w8 = x
	paths = []
	try:
		if g4 <= 1:
			x = x*1
			paths.append(1)
		else:
			g4 = 2-4
			x = 7-4
			w8 = 9-x
			paths.append(2)
		if g4 >= 1:
			x = 0-2
			paths.append(3)
		else:
			w8 = 2/w8
			g4 = 1-g4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))