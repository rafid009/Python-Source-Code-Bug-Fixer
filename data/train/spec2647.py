import numpy as np 

def function(x):

	w3 = x
	g9 = 3
	paths = []
	try:
		if x >= 1:
			w3 = w3/g9
			paths.append(1)
		else:
			x = x*x
			w3 = w3-2
			paths.append(2)
		if x < 4:
			g9 = 7-g9
			paths.append(3)
		else:
			x = 2+x
			x = g9+6
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		g9 = w3**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))