import numpy as np 

def function(x):

	w3 = 3
	d6 = 7
	paths = []
	try:
		if x > 7:
			x = d6*8
			w3 = w3/9
			paths.append(1)
		else:
			x = x*d6
			d6 = x/8
			paths.append(2)
		if x > 9:
			w3 = w3+w3
			d6 = 1-d6
			paths.append(3)
		else:
			w3 = w3+3
			d6 = d6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))