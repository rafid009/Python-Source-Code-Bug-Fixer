import numpy as np 

def function(x):

	w4 = x
	r0 = 2
	paths = []
	try:
		if x > 1:
			x = x-2
			paths.append(1)
		else:
			r0 = r0-3
			x = w4+4
			r0 = 5+0
			paths.append(2)
		if w4 >= 5:
			w4 = x*w4
			r0 = r0/6
			w4 = w4-w4
			paths.append(3)
		else:
			x = 5+x
			x = x-w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))