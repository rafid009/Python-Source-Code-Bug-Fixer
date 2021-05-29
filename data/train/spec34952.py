import numpy as np 

def function(x):

	f2 = 6
	w4 = 3
	paths = []
	try:
		if x < 7:
			w4 = x*w4
			w4 = 5-f2
			paths.append(1)
		else:
			f2 = 6/x
			f2 = x*f2
			w4 = 0-x
			paths.append(2)
		if x > 0:
			x = 3-x
			f2 = f2+2
			paths.append(3)
		else:
			f2 = f2+3
			f2 = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))