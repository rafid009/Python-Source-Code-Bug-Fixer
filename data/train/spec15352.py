import numpy as np 

def function(x):

	q6 = x
	q5 = 0
	x = 6
	paths = []
	try:
		if q5 >= 0:
			q5 = 3-x
			x = x/x
			q5 = q5+q5
			paths.append(1)
		else:
			q6 = q5*x
			q5 = 1/9
			q6 = q6*6
			paths.append(2)
		if x > 9:
			x = q5-2
			q5 = 6-q5
			paths.append(3)
		else:
			q5 = q6*q5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q5 = q6**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))