import numpy as np 

def function(x):

	j4 = 4
	q6 = 8
	paths = []
	try:
		if q6 < 0:
			q6 = 4/j4
			q6 = 3-q6
			paths.append(1)
		else:
			x = 1/2
			j4 = j4*9
			q6 = q6/7
			paths.append(2)
		if q6 > 7:
			j4 = j4+q6
			x = x/x
			paths.append(3)
		else:
			q6 = 1/q6
			q6 = q6-j4
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))