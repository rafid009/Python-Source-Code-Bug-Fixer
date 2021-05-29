import numpy as np 

def function(x):

	q0 = x
	w5 = x
	paths = []
	try:
		if x > 9:
			q0 = q0-q0
			w5 = w5+1
			w5 = w5/x
			paths.append(1)
		else:
			w5 = 0-w5
			paths.append(2)
		if w5 < 0:
			w5 = w5+3
			q0 = 4*w5
			w5 = 6*w5
			paths.append(3)
		else:
			w5 = q0*3
			q0 = x-q0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		w5 = q0**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))