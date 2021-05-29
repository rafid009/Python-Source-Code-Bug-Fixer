import numpy as np 

def function(x):

	q1 = x
	x9 = 3
	paths = []
	try:
		if q1 < 8:
			x9 = x*5
			x9 = x9/q1
			paths.append(1)
		else:
			q1 = 7*6
			paths.append(2)
		if q1 > 1:
			x9 = x/q1
			q1 = q1-8
			x = x9-6
			paths.append(3)
		else:
			x9 = x9-9
			q1 = q1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))