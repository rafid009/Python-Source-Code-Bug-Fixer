import numpy as np 

def function(x):

	q6 = x
	k1 = 0
	paths = []
	try:
		if x < 9:
			q6 = 1+q6
			paths.append(1)
		else:
			k1 = k1+k1
			x = q6-x
			paths.append(2)
		if x <= 2:
			q6 = q6/4
			k1 = k1-2
			paths.append(3)
		else:
			k1 = 0-k1
			q6 = x/9
			q6 = q6-q6
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