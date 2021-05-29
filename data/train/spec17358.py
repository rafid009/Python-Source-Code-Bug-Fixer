import numpy as np 

def function(x):

	w3 = x
	d1 = 8
	x = 1
	paths = []
	try:
		if x <= 1:
			x = x+w3
			x = 8*x
			paths.append(1)
		else:
			w3 = w3-x
			d1 = d1+2
			paths.append(2)
		if w3 > 6:
			w3 = 8/1
			w3 = x+6
			paths.append(3)
		else:
			w3 = w3-w3
			x = 8+x
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))