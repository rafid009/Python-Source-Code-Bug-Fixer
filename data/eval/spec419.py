import numpy as np 

def function(x):

	y8 = x
	q7 = x
	x = x
	paths = []
	try:
		if x > 0:
			q7 = 0+x
			q7 = q7/2
			x = 5-q7
			paths.append(1)
		else:
			y8 = 4/y8
			y8 = y8*y8
			paths.append(2)
		if x >= 1:
			x = x/3
			y8 = y8/7
			paths.append(3)
		else:
			x = 5/y8
			x = 5-x
			y8 = 1*q7
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