import numpy as np 

def function(x):

	q1 = x
	x0 = x
	paths = []
	try:
		if x0 <= 6:
			q1 = q1/7
			x0 = x0-q1
			paths.append(1)
		else:
			x = q1-x
			q1 = q1-q1
			paths.append(2)
		if x0 <= 8:
			q1 = q1+5
			paths.append(3)
		else:
			q1 = x0+7
			q1 = q1+9
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))