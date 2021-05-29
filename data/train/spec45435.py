import numpy as np 

def function(x):

	q2 = 5
	v1 = x
	paths = []
	try:
		if q2 < 2:
			q2 = 2+9
			paths.append(1)
		else:
			q2 = 7-v1
			paths.append(2)
		if v1 < 6:
			q2 = q2/3
			v1 = v1+3
			paths.append(3)
		else:
			x = 1-8
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