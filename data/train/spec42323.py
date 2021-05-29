import numpy as np 

def function(x):

	q1 = x
	l9 = 0
	paths = []
	try:
		if x <= 0:
			l9 = 6*8
			paths.append(1)
		else:
			x = x-4
			l9 = l9+7
			paths.append(2)
		if x <= 9:
			l9 = l9/1
			l9 = l9/q1
			paths.append(3)
		else:
			q1 = 2+q1
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