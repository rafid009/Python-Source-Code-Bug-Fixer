import numpy as np 

def function(x):

	q6 = x
	k4 = x
	paths = []
	try:
		if q6 >= 2:
			q6 = q6/2
			paths.append(1)
		else:
			x = 5+7
			k4 = k4-1
			paths.append(2)
		if x < 4:
			x = x-1
			q6 = q6*6
			k4 = x*k4
			paths.append(3)
		else:
			k4 = 3/k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		q6 = k4**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))