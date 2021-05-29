import numpy as np 

def function(x):

	g3 = 1
	w8 = x
	paths = []
	try:
		if x <= 7:
			w8 = x+8
			w8 = g3-w8
			g3 = g3/3
			paths.append(1)
		else:
			g3 = 8-g3
			g3 = g3/6
			x = g3/x
			paths.append(2)
		if w8 >= 8:
			g3 = 4-g3
			w8 = 6-g3
			g3 = g3-8
			paths.append(3)
		else:
			w8 = w8+0
			x = 9/x
			g3 = 3-7
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		g3 = w8**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))