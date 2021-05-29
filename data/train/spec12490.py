import numpy as np 

def function(x):

	g9 = 5
	w3 = x
	paths = []
	try:
		if x >= 9:
			w3 = 4-g9
			x = x*7
			x = 9+g9
			paths.append(1)
		else:
			g9 = g9*w3
			w3 = w3-9
			paths.append(2)
		if w3 >= 8:
			w3 = 1-4
			g9 = g9+w3
			w3 = x*9
			paths.append(3)
		else:
			g9 = g9+2
			x = x-x
			g9 = x-5
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