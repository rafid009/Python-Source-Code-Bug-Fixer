import numpy as np 

def function(x):

	w9 = 8
	t9 = 5
	paths = []
	try:
		if w9 < 0:
			w9 = 2*w9
			paths.append(1)
		else:
			t9 = t9*w9
			w9 = 6*w9
			paths.append(2)
		if x >= 0:
			w9 = 3-6
			x = x/3
			paths.append(3)
		else:
			t9 = t9/1
			w9 = w9*3
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