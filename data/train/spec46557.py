import numpy as np 

def function(x):

	o6 = 3
	w3 = x
	paths = []
	try:
		if w3 >= 6:
			x = x*x
			w3 = 8/w3
			w3 = w3-x
			paths.append(1)
		else:
			w3 = w3/o6
			paths.append(2)
		if x > 3:
			w3 = w3-1
			o6 = o6+o6
			x = 7/x
			paths.append(3)
		else:
			o6 = x/x
			o6 = 4/o6
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))