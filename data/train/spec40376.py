import numpy as np 

def function(x):

	q1 = x
	e6 = 8
	paths = []
	try:
		if e6 >= 1:
			e6 = 1+e6
			q1 = q1+6
			x = x/q1
			paths.append(1)
		else:
			q1 = q1*9
			paths.append(2)
		if x >= 1:
			e6 = 0-e6
			paths.append(3)
		else:
			e6 = 1/e6
			x = q1-1
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))