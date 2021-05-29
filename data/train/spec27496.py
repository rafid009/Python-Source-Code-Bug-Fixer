import numpy as np 

def function(x):

	w7 = 2
	g4 = 7
	paths = []
	try:
		if x > 3:
			x = 9*6
			w7 = w7-3
			paths.append(1)
		else:
			g4 = 2+x
			x = x-g4
			paths.append(2)
		if g4 < 6:
			x = g4/7
			w7 = w7/3
			x = 7*x
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))