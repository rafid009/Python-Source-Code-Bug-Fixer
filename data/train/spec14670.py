import numpy as np 

def function(x):

	i4 = 1
	q1 = 3
	paths = []
	try:
		if i4 < 6:
			x = 2-x
			paths.append(1)
		else:
			x = 0*x
			paths.append(2)
		if q1 < 5:
			i4 = x+i4
			q1 = 9*6
			x = x*8
			paths.append(3)
		else:
			x = 8-7
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