import numpy as np 

def function(x):

	w8 = 3
	g7 = x
	paths = []
	try:
		if g7 >= 2:
			x = 2-g7
			w8 = 2+w8
			paths.append(1)
		else:
			w8 = 5/7
			w8 = 3-w8
			x = x*2
			paths.append(2)
		if x >= 4:
			w8 = 8-g7
			g7 = 3/g7
			w8 = w8/9
			paths.append(3)
		else:
			w8 = w8*x
			w8 = 3+g7
			g7 = 3/g7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))