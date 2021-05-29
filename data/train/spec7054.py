import numpy as np 

def function(x):

	q8 = 7
	r1 = 5
	paths = []
	try:
		if q8 > 1:
			r1 = r1/7
			r1 = 9/r1
			paths.append(1)
		else:
			q8 = 2*7
			paths.append(2)
		if r1 <= 0:
			x = x-r1
			paths.append(3)
		else:
			r1 = r1-2
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