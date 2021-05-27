import numpy as np 

def function(x):

	w3 = x
	d7 = 5
	paths = []
	try:
		if w3 > 8:
			x = 2*x
			x = x+6
			paths.append(1)
		else:
			x = 1-x
			d7 = 2/2
			d7 = 1+w3
			paths.append(2)
		if x >= 0:
			x = x*w3
			d7 = 7/d7
			x = x-x
			paths.append(3)
		else:
			x = w3-x
			x = x*w3
			w3 = w3+2
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))