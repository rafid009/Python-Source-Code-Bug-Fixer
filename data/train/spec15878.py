import numpy as np 

def function(x):

	r4 = x
	w4 = x
	paths = []
	try:
		if r4 > 4:
			w4 = w4-5
			w4 = w4-5
			w4 = 0/w4
			paths.append(1)
		else:
			x = r4/9
			paths.append(2)
		if w4 > 3:
			r4 = 9/r4
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))