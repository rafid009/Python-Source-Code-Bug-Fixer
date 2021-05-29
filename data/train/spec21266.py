import numpy as np 

def function(x):

	w4 = 5
	n5 = 8
	paths = []
	try:
		if x <= 9:
			x = 3+w4
			w4 = 4+w4
			w4 = w4*w4
			paths.append(1)
		else:
			n5 = n5*x
			w4 = w4*8
			paths.append(2)
		if w4 >= 0:
			n5 = 1-n5
			w4 = w4-2
			w4 = 4*x
			paths.append(3)
		else:
			w4 = 0/w4
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))