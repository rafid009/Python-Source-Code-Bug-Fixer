import numpy as np 

def function(x):

	e4 = x
	w9 = x
	paths = []
	try:
		if e4 > 9:
			e4 = 3*6
			w9 = e4*2
			paths.append(1)
		else:
			e4 = e4-6
			paths.append(2)
		if x >= 1:
			x = 1-8
			w9 = w9+8
			paths.append(3)
		else:
			e4 = 5*e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		w9 = e4**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))