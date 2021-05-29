import numpy as np 

def function(x):

	w8 = 9
	r2 = x
	paths = []
	try:
		if w8 <= 9:
			r2 = 3-r2
			x = x/8
			paths.append(1)
		else:
			r2 = r2/x
			paths.append(2)
		if w8 < 8:
			r2 = w8/r2
			paths.append(3)
		else:
			w8 = r2*x
			x = x-9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		w8 = r2**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))