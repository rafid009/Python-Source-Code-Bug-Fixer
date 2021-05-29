import numpy as np 

def function(x):

	q8 = x
	o4 = x
	paths = []
	try:
		if q8 < 1:
			q8 = 4*q8
			paths.append(1)
		else:
			q8 = 0-q8
			q8 = o4/3
			q8 = q8/4
			paths.append(2)
		if q8 > 1:
			q8 = q8*3
			paths.append(3)
		else:
			q8 = 1-q8
			q8 = q8+3
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		q8 = o4**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))