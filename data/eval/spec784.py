import numpy as np 

def function(x):

	w3 = x
	g9 = 9
	x = 1
	paths = []
	try:
		if w3 <= 9:
			g9 = g9*g9
			paths.append(1)
		else:
			x = x-g9
			w3 = 8-w3
			paths.append(2)
		if g9 < 1:
			w3 = 8-3
			g9 = g9/g9
			paths.append(3)
		else:
			x = 7*x
			g9 = 3/g9
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))