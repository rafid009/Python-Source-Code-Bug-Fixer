import numpy as np 

def function(x):

	q6 = 8
	q9 = x
	paths = []
	try:
		if x >= 7:
			q6 = q6+2
			q6 = 1+3
			paths.append(1)
		else:
			q9 = 7+q9
			paths.append(2)
		if x > 8:
			q9 = x-3
			paths.append(3)
		else:
			q9 = 2/4
			q9 = 9-4
			q9 = q9-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))