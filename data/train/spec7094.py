import numpy as np 

def function(x):

	w7 = 6
	g4 = 9
	paths = []
	try:
		if g4 >= 9:
			w7 = w7-7
			x = 4/x
			g4 = g4/3
			paths.append(1)
		else:
			g4 = 4/g4
			g4 = 6*3
			w7 = w7/1
			paths.append(2)
		if g4 < 2:
			w7 = w7+x
			w7 = w7/x
			paths.append(3)
		else:
			x = x*6
			g4 = g4-9
			w7 = w7/5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))