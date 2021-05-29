import numpy as np 

def function(x):

	q0 = 4
	w8 = x
	paths = []
	try:
		if q0 > 9:
			q0 = 3-q0
			q0 = q0+1
			w8 = 7-w8
			paths.append(1)
		else:
			x = q0*x
			paths.append(2)
		if q0 >= 6:
			x = 0-x
			w8 = w8-1
			paths.append(3)
		else:
			q0 = x*2
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))