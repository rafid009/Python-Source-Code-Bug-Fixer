import numpy as np 

def function(x):

	g4 = 3
	w5 = 3
	paths = []
	try:
		if g4 < 2:
			g4 = g4/7
			g4 = 5-1
			paths.append(1)
		else:
			w5 = w5+3
			x = x*g4
			g4 = w5/w5
			paths.append(2)
		if w5 >= 6:
			w5 = w5/2
			paths.append(3)
		else:
			g4 = g4+x
			w5 = 4-w5
			x = w5/w5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))