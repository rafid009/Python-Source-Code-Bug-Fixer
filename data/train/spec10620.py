import numpy as np 

def function(x):

	r5 = x
	w4 = 5
	paths = []
	try:
		if w4 >= 9:
			r5 = 9/7
			paths.append(1)
		else:
			r5 = 0+8
			w4 = 5*w4
			r5 = 2*r5
			paths.append(2)
		if x >= 5:
			x = 8*x
			x = 7-x
			paths.append(3)
		else:
			w4 = w4-8
			r5 = r5-w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))