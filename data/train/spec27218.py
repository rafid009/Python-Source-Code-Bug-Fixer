import numpy as np 

def function(x):

	w4 = x
	b9 = 8
	paths = []
	try:
		if x < 2:
			b9 = b9/3
			x = x-1
			paths.append(1)
		else:
			w4 = 3*w4
			w4 = 7+w4
			x = 5-w4
			paths.append(2)
		if b9 < 7:
			w4 = w4*1
			w4 = 5*w4
			b9 = b9-3
			paths.append(3)
		else:
			b9 = w4-b9
			b9 = 8/5
			w4 = w4+2
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