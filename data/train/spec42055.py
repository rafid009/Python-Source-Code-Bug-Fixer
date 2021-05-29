import numpy as np 

def function(x):

	x7 = 9
	w3 = 5
	paths = []
	try:
		if x < 9:
			x = x7-3
			w3 = w3*3
			w3 = 1-w3
			paths.append(1)
		else:
			x = x/w3
			x7 = x7-6
			paths.append(2)
		if x >= 9:
			x7 = x7-x7
			w3 = w3*2
			x7 = 7-x
			paths.append(3)
		else:
			x7 = 2*x7
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x7 = w3**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))