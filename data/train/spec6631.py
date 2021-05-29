import numpy as np 

def function(x):

	a9 = x
	w3 = x
	paths = []
	try:
		if x < 4:
			w3 = w3+2
			a9 = a9/6
			paths.append(1)
		else:
			w3 = x/3
			a9 = a9/7
			w3 = w3*3
			paths.append(2)
		if w3 > 4:
			w3 = w3-5
			x = 2*x
			paths.append(3)
		else:
			w3 = 1/w3
			a9 = a9*w3
			x = x/w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))