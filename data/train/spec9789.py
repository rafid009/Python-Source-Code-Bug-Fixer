import numpy as np 

def function(x):

	w9 = x
	o7 = x
	paths = []
	try:
		if x <= 0:
			o7 = 9-0
			w9 = w9+4
			x = 3/x
			paths.append(1)
		else:
			o7 = o7-5
			o7 = w9-x
			o7 = 4-o7
			paths.append(2)
		if w9 < 4:
			x = o7/x
			o7 = o7/x
			paths.append(3)
		else:
			w9 = 4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))