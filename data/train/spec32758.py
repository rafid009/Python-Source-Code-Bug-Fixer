import numpy as np 

def function(x):

	i9 = 6
	q1 = 1
	paths = []
	try:
		if x < 4:
			i9 = 0*7
			x = 3-x
			paths.append(1)
		else:
			x = 3/7
			q1 = q1/5
			paths.append(2)
		if x >= 5:
			i9 = i9/4
			paths.append(3)
		else:
			q1 = 8*q1
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