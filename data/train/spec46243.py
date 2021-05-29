import numpy as np 

def function(x):

	q5 = 3
	k4 = 1
	paths = []
	try:
		if x >= 3:
			x = q5+3
			q5 = k4+2
			paths.append(1)
		else:
			k4 = k4-k4
			paths.append(2)
		if q5 <= 3:
			k4 = 5*x
			paths.append(3)
		else:
			q5 = k4*6
			q5 = q5-1
			k4 = x-k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		q5 = k4**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))