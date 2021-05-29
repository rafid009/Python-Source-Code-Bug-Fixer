import numpy as np 

def function(x):

	w6 = 9
	i8 = x
	paths = []
	try:
		if w6 < 6:
			x = i8-w6
			i8 = i8/i8
			i8 = x-i8
			paths.append(1)
		else:
			w6 = w6-i8
			w6 = w6-8
			paths.append(2)
		if x <= 0:
			w6 = w6-i8
			paths.append(3)
		else:
			x = 1*w6
			w6 = 0-w6
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