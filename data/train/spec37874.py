import numpy as np 

def function(x):

	w3 = 3
	w8 = x
	paths = []
	try:
		if x > 6:
			w3 = w3+9
			w8 = w8*x
			paths.append(1)
		else:
			w8 = x*w3
			w3 = 6/w3
			paths.append(2)
		if w3 > 2:
			w8 = 2-9
			paths.append(3)
		else:
			x = x*8
			w3 = 9/2
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