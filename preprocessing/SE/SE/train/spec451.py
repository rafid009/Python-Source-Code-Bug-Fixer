import numpy as np 

def function(x):

	q7 = 0
	v7 = x
	paths = []
	try:
		if v7 >= 7:
			q7 = q7/6
			q7 = 2*v7
			paths.append(1)
		else:
			v7 = x/6
			q7 = 7-q7
			paths.append(2)
		if q7 >= 3:
			x = 5*x
			x = x-5
			x = v7*7
			paths.append(3)
		else:
			q7 = q7/q7
			x = 1/v7
			v7 = v7-5
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