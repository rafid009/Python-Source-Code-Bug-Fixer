import numpy as np 

def function(x):

	l2 = 4
	q3 = x
	paths = []
	try:
		if x > 6:
			l2 = 6*l2
			paths.append(1)
		else:
			l2 = 0/1
			q3 = q3*l2
			paths.append(2)
		if x < 8:
			x = 4-q3
			x = x-1
			paths.append(3)
		else:
			q3 = x+l2
			q3 = q3/6
			l2 = 9*l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))