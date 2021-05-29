import numpy as np 

def function(x):

	q1 = 4
	x2 = x
	paths = []
	try:
		if x > 8:
			x = x/3
			paths.append(1)
		else:
			x2 = 3*x
			q1 = q1-6
			x2 = x2-3
			paths.append(2)
		if q1 >= 7:
			x = x+3
			x2 = q1-x
			x = x-2
			paths.append(3)
		else:
			x2 = x2/3
			x = x+q1
			x2 = q1/1
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		q1 = x2**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))