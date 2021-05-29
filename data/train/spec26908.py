import numpy as np 

def function(x):

	q7 = x
	e6 = 0
	x = 1
	paths = []
	try:
		if x >= 8:
			x = x*4
			paths.append(1)
		else:
			q7 = q7*x
			paths.append(2)
		if x >= 7:
			e6 = x*e6
			q7 = q7/7
			paths.append(3)
		else:
			e6 = 2-9
			x = x-8
			e6 = e6/4
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