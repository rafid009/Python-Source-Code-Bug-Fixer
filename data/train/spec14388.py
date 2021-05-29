import numpy as np 

def function(x):

	w3 = 5
	w8 = 7
	paths = []
	try:
		if x <= 9:
			w8 = w3+w3
			w8 = 2*w8
			paths.append(1)
		else:
			x = 4*6
			paths.append(2)
		if x >= 9:
			x = x*x
			w3 = 4-w3
			paths.append(3)
		else:
			w8 = 1*w8
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