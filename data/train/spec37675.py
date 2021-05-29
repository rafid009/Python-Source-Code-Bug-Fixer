import numpy as np 

def function(x):

	w4 = x
	r3 = 3
	paths = []
	try:
		if w4 <= 3:
			x = w4-x
			paths.append(1)
		else:
			x = 2-7
			paths.append(2)
		if x > 5:
			r3 = r3-5
			paths.append(3)
		else:
			w4 = w4*2
			r3 = 7/r3
			r3 = x-4
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