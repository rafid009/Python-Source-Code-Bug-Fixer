import numpy as np 

def function(x):

	a5 = 1
	q1 = 9
	paths = []
	try:
		if x <= 1:
			q1 = q1*a5
			q1 = 0+3
			a5 = 5-a5
			paths.append(1)
		else:
			a5 = q1-8
			a5 = 8-8
			x = a5*q1
			paths.append(2)
		if q1 <= 8:
			a5 = a5-6
			paths.append(3)
		else:
			q1 = 4*3
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		q1 = a5**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))