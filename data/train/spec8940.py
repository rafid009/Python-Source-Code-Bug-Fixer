import numpy as np 

def function(x):

	w4 = 6
	q8 = 9
	paths = []
	try:
		if q8 > 8:
			q8 = x/q8
			w4 = 3+8
			paths.append(1)
		else:
			x = 0*x
			q8 = w4+q8
			q8 = q8*8
			paths.append(2)
		if w4 > 2:
			w4 = 8-5
			q8 = 4-6
			x = x-0
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		w4 = q8**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))