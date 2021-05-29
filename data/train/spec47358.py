import numpy as np 

def function(x):

	g5 = 1
	w3 = x
	paths = []
	try:
		if x > 6:
			x = x/w3
			x = 9*x
			g5 = g5-4
			paths.append(1)
		else:
			x = 1/x
			w3 = 9+w3
			x = g5+w3
			paths.append(2)
		if g5 < 1:
			g5 = g5*g5
			paths.append(3)
		else:
			g5 = g5/3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w3 = w3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))