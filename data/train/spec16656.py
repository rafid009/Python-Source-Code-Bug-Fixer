import numpy as np 

def function(x):

	x1 = x
	q1 = 4
	paths = []
	try:
		if x1 >= 8:
			q1 = 8/q1
			x1 = x1+0
			x = x-1
			paths.append(1)
		else:
			q1 = q1*6
			paths.append(2)
		if q1 <= 7:
			x = 0/7
			x = 3*3
			paths.append(3)
		else:
			q1 = q1+5
			x1 = q1+q1
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