import numpy as np 

def function(x):

	q4 = x
	q6 = 1
	paths = []
	try:
		if q4 <= 3:
			q6 = 0/q6
			x = 3/x
			x = x-6
			paths.append(1)
		else:
			q6 = q6-q4
			paths.append(2)
		if x > 5:
			x = x+q6
			q6 = q6-5
			q6 = x/6
			paths.append(3)
		else:
			x = x-0
			x = q6/x
			q6 = 3*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))