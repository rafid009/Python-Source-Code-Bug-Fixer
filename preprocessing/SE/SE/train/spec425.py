import numpy as np 

def function(x):

	q8 = 7
	n0 = 4
	paths = []
	try:
		if q8 > 4:
			n0 = 2/x
			q8 = 5*x
			paths.append(1)
		else:
			x = 3-2
			paths.append(2)
		if n0 > 5:
			x = x-n0
			n0 = 2+n0
			n0 = q8-n0
			paths.append(3)
		else:
			q8 = 1-q8
			n0 = 4-q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		n0 = q8**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))