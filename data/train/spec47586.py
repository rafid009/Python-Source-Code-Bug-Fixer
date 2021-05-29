import numpy as np 

def function(x):

	q6 = 5
	o9 = 8
	paths = []
	try:
		if q6 > 8:
			o9 = 2+6
			q6 = 9*q6
			o9 = o9+x
			paths.append(1)
		else:
			o9 = o9*8
			x = 7+x
			paths.append(2)
		if x < 0:
			q6 = 9*q6
			paths.append(3)
		else:
			o9 = x-6
			q6 = 1*q6
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))