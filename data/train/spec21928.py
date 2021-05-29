import numpy as np 

def function(x):

	q6 = x
	o9 = 1
	paths = []
	try:
		if x > 1:
			x = o9*x
			paths.append(1)
		else:
			o9 = o9-7
			paths.append(2)
		if q6 >= 1:
			q6 = 0-q6
			o9 = q6/o9
			paths.append(3)
		else:
			x = x/1
			x = 8+q6
			q6 = q6-1
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