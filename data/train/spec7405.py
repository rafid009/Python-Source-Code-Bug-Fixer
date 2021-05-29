import numpy as np 

def function(x):

	w5 = x
	g4 = 6
	x = x
	paths = []
	try:
		if w5 > 5:
			g4 = x-w5
			g4 = g4*w5
			w5 = w5-w5
			paths.append(1)
		else:
			g4 = 1/g4
			g4 = 2+5
			paths.append(2)
		if g4 < 1:
			g4 = g4-x
			w5 = w5*8
			x = w5+x
			paths.append(3)
		else:
			w5 = w5/w5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))