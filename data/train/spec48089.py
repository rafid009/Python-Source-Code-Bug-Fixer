import numpy as np 

def function(x):

	i9 = 5
	q1 = 3
	x = x
	paths = []
	try:
		if x < 7:
			i9 = i9*8
			paths.append(1)
		else:
			i9 = 2+6
			q1 = q1*3
			paths.append(2)
		if x > 6:
			q1 = q1-9
			paths.append(3)
		else:
			x = 6*x
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