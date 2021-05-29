import numpy as np 

def function(x):

	g6 = 8
	w5 = x
	x = x
	paths = []
	try:
		if x < 9:
			w5 = w5-0
			w5 = w5+w5
			g6 = g6*w5
			paths.append(1)
		else:
			g6 = g6/3
			paths.append(2)
		if w5 > 9:
			w5 = 0/g6
			w5 = 9-4
			paths.append(3)
		else:
			g6 = w5*g6
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))