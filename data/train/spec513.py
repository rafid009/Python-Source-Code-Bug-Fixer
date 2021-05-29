import numpy as np 

def function(x):

	q1 = 5
	k7 = 6
	paths = []
	try:
		if x >= 8:
			x = x-x
			q1 = 0*q1
			paths.append(1)
		else:
			q1 = q1/x
			paths.append(2)
		if q1 > 1:
			x = 4-x
			q1 = 9*k7
			paths.append(3)
		else:
			q1 = q1+2
			k7 = q1+2
			q1 = q1+k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))