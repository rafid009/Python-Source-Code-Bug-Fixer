import numpy as np 

def function(x):

	w4 = x
	o5 = x
	paths = []
	try:
		if x < 4:
			o5 = o5*w4
			paths.append(1)
		else:
			w4 = 2-w4
			w4 = w4/2
			o5 = 9+3
			paths.append(2)
		if o5 < 3:
			o5 = 8-o5
			o5 = 9-o5
			o5 = o5*w4
			paths.append(3)
		else:
			o5 = o5/o5
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