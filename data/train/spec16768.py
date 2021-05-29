import numpy as np 

def function(x):

	q9 = x
	q8 = 6
	paths = []
	try:
		if q8 > 4:
			q9 = 6*3
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if q8 < 4:
			q9 = 5*q9
			x = q9*q9
			paths.append(3)
		else:
			q9 = 3*q9
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))