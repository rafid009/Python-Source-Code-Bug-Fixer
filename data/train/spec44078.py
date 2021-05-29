import numpy as np 

def function(x):

	n1 = 0
	q8 = x
	paths = []
	try:
		if n1 >= 0:
			x = 6-x
			q8 = 8/q8
			q8 = 0*7
			paths.append(1)
		else:
			x = 1*9
			x = x-n1
			q8 = q8+4
			paths.append(2)
		if q8 < 5:
			q8 = q8-x
			n1 = q8*n1
			x = 2+x
			paths.append(3)
		else:
			q8 = q8+q8
			q8 = 3+n1
			n1 = q8/1
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