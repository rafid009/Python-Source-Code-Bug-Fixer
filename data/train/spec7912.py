import numpy as np 

def function(x):

	q2 = x
	z7 = x
	paths = []
	try:
		if q2 < 8:
			x = 5/x
			paths.append(1)
		else:
			q2 = q2+8
			q2 = q2-4
			paths.append(2)
		if z7 > 3:
			q2 = q2*6
			x = z7-9
			x = 1*z7
			paths.append(3)
		else:
			x = z7-3
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