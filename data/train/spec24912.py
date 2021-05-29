import numpy as np 

def function(x):

	j4 = 7
	q6 = 8
	paths = []
	try:
		if x >= 6:
			q6 = q6+q6
			j4 = j4+x
			q6 = q6*3
			paths.append(1)
		else:
			j4 = 3-6
			j4 = j4/1
			paths.append(2)
		if x < 0:
			q6 = q6*x
			q6 = j4/4
			j4 = 5*j4
			paths.append(3)
		else:
			q6 = 3*q6
			x = 1/j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))