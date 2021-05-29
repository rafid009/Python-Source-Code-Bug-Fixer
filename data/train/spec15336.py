import numpy as np 

def function(x):

	w4 = x
	u2 = 1
	paths = []
	try:
		if x < 4:
			u2 = 6*3
			paths.append(1)
		else:
			u2 = x+9
			w4 = x-w4
			paths.append(2)
		if u2 > 8:
			w4 = 2-w4
			paths.append(3)
		else:
			w4 = w4/8
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