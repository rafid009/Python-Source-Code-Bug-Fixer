import numpy as np 

def function(x):

	w4 = 2
	o0 = x
	x = x
	paths = []
	try:
		if x <= 1:
			x = 8/3
			paths.append(1)
		else:
			o0 = 3/o0
			paths.append(2)
		if x >= 1:
			o0 = w4-5
			o0 = 2/o0
			paths.append(3)
		else:
			w4 = w4-4
			w4 = 8+0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		w4 = o0**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))