import numpy as np 

def function(x):

	n6 = 6
	q7 = x
	paths = []
	try:
		if x < 6:
			n6 = q7/q7
			q7 = q7/5
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if q7 > 4:
			x = x*3
			n6 = 4-7
			n6 = 1/9
			paths.append(3)
		else:
			n6 = n6-x
			q7 = 2*q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))