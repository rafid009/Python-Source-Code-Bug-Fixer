import numpy as np 

def function(x):

	q5 = 3
	q6 = x
	paths = []
	try:
		if q6 < 2:
			q5 = q5-7
			x = x-5
			paths.append(1)
		else:
			q6 = 4-q6
			q6 = 0*q6
			q5 = q5*x
			paths.append(2)
		if q6 < 6:
			x = 8-x
			x = x*8
			paths.append(3)
		else:
			q5 = q6/q5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))