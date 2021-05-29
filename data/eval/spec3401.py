import numpy as np 

def function(x):

	a7 = 8
	q1 = 3
	paths = []
	try:
		if x >= 7:
			a7 = a7/x
			q1 = 1+q1
			a7 = 2/x
			paths.append(1)
		else:
			a7 = q1-a7
			paths.append(2)
		if q1 < 6:
			x = x/9
			a7 = a7*q1
			x = a7/6
			paths.append(3)
		else:
			x = x+1
			a7 = x-a7
			q1 = 6-q1
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		q1 = a7**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))