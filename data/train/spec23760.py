import numpy as np 

def function(x):

	q1 = x
	e6 = 9
	paths = []
	try:
		if x >= 6:
			x = e6/e6
			paths.append(1)
		else:
			q1 = 5*9
			e6 = e6-e6
			q1 = 9-q1
			paths.append(2)
		if q1 >= 4:
			x = x/5
			q1 = 4*q1
			paths.append(3)
		else:
			x = 5-x
			e6 = 2-9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))