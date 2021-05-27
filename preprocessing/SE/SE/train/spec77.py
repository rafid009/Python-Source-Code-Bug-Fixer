import numpy as np 

def function(x):

	e7 = 1
	q2 = 5
	paths = []
	try:
		if x > 7:
			x = x*q2
			x = e7/3
			paths.append(1)
		else:
			q2 = q2-q2
			paths.append(2)
		if q2 >= 4:
			e7 = q2-2
			paths.append(3)
		else:
			q2 = q2+x
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