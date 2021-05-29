import numpy as np 

def function(x):

	q7 = 9
	n7 = x
	x = 6
	paths = []
	try:
		if x >= 0:
			x = n7/x
			paths.append(1)
		else:
			n7 = n7*9
			x = x*5
			n7 = n7-8
			paths.append(2)
		if x <= 0:
			x = x/2
			n7 = n7*q7
			n7 = n7+n7
			paths.append(3)
		else:
			q7 = q7+8
			x = n7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))