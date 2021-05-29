import numpy as np 

def function(x):

	q6 = 3
	j4 = 4
	paths = []
	try:
		if j4 > 1:
			x = 9*x
			q6 = 7*x
			paths.append(1)
		else:
			j4 = q6+5
			paths.append(2)
		if x >= 7:
			x = x+0
			q6 = 9+q6
			x = 7/4
			paths.append(3)
		else:
			j4 = q6*2
			q6 = q6/j4
			q6 = q6-9
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