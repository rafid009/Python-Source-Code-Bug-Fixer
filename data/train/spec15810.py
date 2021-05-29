import numpy as np 

def function(x):

	x6 = x
	w3 = 7
	paths = []
	try:
		if w3 <= 5:
			w3 = 3-0
			x = 4+x
			paths.append(1)
		else:
			w3 = 1/6
			x6 = 3*x6
			paths.append(2)
		if w3 > 8:
			w3 = 1-w3
			paths.append(3)
		else:
			w3 = x+w3
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