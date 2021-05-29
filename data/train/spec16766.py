import numpy as np 

def function(x):

	w7 = 0
	y5 = 0
	x = x
	paths = []
	try:
		if w7 >= 9:
			y5 = y5-8
			w7 = 9+w7
			w7 = w7/x
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if w7 <= 4:
			y5 = 9-y5
			paths.append(3)
		else:
			w7 = y5/y5
			w7 = 0+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))