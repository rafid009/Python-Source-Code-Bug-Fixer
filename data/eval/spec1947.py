import numpy as np 

def function(x):

	q6 = x
	o7 = 7
	x = 8
	paths = []
	try:
		if x <= 7:
			q6 = 1/1
			q6 = 0*q6
			paths.append(1)
		else:
			q6 = 7/8
			o7 = 6-x
			paths.append(2)
		if q6 < 2:
			q6 = o7*q6
			paths.append(3)
		else:
			o7 = o7/5
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		q6 = o7**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))