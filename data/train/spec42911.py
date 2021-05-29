import numpy as np 

def function(x):

	w4 = 9
	r4 = 1
	paths = []
	try:
		if w4 < 8:
			x = x+r4
			paths.append(1)
		else:
			r4 = r4*5
			r4 = r4-5
			paths.append(2)
		if r4 > 3:
			w4 = w4-9
			paths.append(3)
		else:
			w4 = w4*9
			w4 = w4-x
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