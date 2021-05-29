import numpy as np 

def function(x):

	q1 = x
	v5 = x
	paths = []
	try:
		if x > 4:
			v5 = v5-v5
			paths.append(1)
		else:
			q1 = 7/1
			paths.append(2)
		if q1 < 8:
			v5 = q1-v5
			q1 = 8*q1
			x = x-0
			paths.append(3)
		else:
			v5 = v5-v5
			v5 = v5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))