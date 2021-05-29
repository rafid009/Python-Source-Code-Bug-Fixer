import numpy as np 

def function(x):

	a7 = 7
	q3 = 4
	paths = []
	try:
		if x >= 5:
			a7 = a7/6
			x = 8/3
			paths.append(1)
		else:
			a7 = a7+x
			paths.append(2)
		if q3 >= 7:
			q3 = 8/x
			x = 2*x
			paths.append(3)
		else:
			x = x/4
			q3 = 6*q3
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		q3 = a7**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))