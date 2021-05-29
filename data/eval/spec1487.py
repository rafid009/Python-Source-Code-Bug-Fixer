import numpy as np 

def function(x):

	q2 = x
	w4 = 3
	paths = []
	try:
		if q2 >= 8:
			w4 = w4-x
			w4 = w4*7
			paths.append(1)
		else:
			x = 8*w4
			w4 = w4+6
			x = 2+x
			paths.append(2)
		if x <= 9:
			x = 1/5
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))