import numpy as np 

def function(x):

	q6 = 7
	j4 = 3
	x = x
	paths = []
	try:
		if q6 > 8:
			x = 7*x
			paths.append(1)
		else:
			j4 = 7*j4
			q6 = q6+5
			q6 = 7+j4
			paths.append(2)
		if x > 1:
			j4 = j4*j4
			paths.append(3)
		else:
			q6 = 7+q6
			q6 = q6/2
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