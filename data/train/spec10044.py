import numpy as np 

def function(x):

	d9 = x
	w3 = x
	paths = []
	try:
		if w3 < 6:
			d9 = x/d9
			paths.append(1)
		else:
			x = 9/x
			w3 = d9/3
			x = 3*x
			paths.append(2)
		if x >= 0:
			d9 = 3+x
			paths.append(3)
		else:
			d9 = 3-d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))