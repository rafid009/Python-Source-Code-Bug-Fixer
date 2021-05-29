import numpy as np 

def function(x):

	w7 = x
	g7 = 7
	paths = []
	try:
		if w7 < 8:
			w7 = w7/6
			paths.append(1)
		else:
			x = 2/x
			x = x+8
			paths.append(2)
		if x < 1:
			w7 = w7*1
			x = 5/x
			paths.append(3)
		else:
			g7 = g7/3
			w7 = 7+w7
			x = x*4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))