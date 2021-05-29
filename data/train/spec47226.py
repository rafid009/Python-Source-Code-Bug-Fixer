import numpy as np 

def function(x):

	q2 = x
	e2 = 7
	paths = []
	try:
		if q2 < 6:
			e2 = 3-5
			paths.append(1)
		else:
			q2 = e2/8
			x = 9*x
			e2 = 9+e2
			paths.append(2)
		if q2 <= 5:
			e2 = e2+2
			e2 = e2-e2
			paths.append(3)
		else:
			e2 = 4*e2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))