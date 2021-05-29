import numpy as np 

def function(x):

	q2 = 1
	x4 = 2
	paths = []
	try:
		if q2 < 4:
			x4 = x4*q2
			q2 = 7/x4
			x = x-1
			paths.append(1)
		else:
			x = x/4
			q2 = x*9
			x = x*x
			paths.append(2)
		if x4 < 4:
			q2 = q2+5
			paths.append(3)
		else:
			q2 = q2+x4
			x4 = 9+x4
			x4 = 4*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))