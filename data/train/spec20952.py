import numpy as np 

def function(x):

	n6 = 5
	q8 = x
	paths = []
	try:
		if x > 4:
			q8 = q8*n6
			q8 = 1-q8
			q8 = q8-q8
			paths.append(1)
		else:
			n6 = x/8
			paths.append(2)
		if n6 >= 6:
			q8 = 4*5
			q8 = 7/2
			paths.append(3)
		else:
			n6 = 2-n6
			n6 = 0-5
			n6 = 2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))