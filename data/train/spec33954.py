import numpy as np 

def function(x):

	w8 = x
	q0 = x
	paths = []
	try:
		if x >= 7:
			w8 = w8/w8
			paths.append(1)
		else:
			w8 = 8/w8
			paths.append(2)
		if q0 < 3:
			w8 = 0+w8
			q0 = 3*q0
			x = w8/x
			paths.append(3)
		else:
			q0 = q0*q0
			w8 = w8+9
			w8 = w8+6
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		w8 = q0**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))