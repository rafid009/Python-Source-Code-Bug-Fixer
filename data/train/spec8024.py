import numpy as np 

def function(x):

	q2 = x
	e1 = 8
	paths = []
	try:
		if x < 2:
			e1 = q2/x
			paths.append(1)
		else:
			e1 = 5-e1
			q2 = q2-4
			paths.append(2)
		if e1 < 1:
			q2 = x+0
			paths.append(3)
		else:
			q2 = 9*q2
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