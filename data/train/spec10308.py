import numpy as np 

def function(x):

	q6 = 3
	n7 = x
	x = 8
	paths = []
	try:
		if q6 <= 2:
			q6 = q6/q6
			paths.append(1)
		else:
			x = 3+5
			paths.append(2)
		if q6 > 6:
			n7 = n7/n7
			paths.append(3)
		else:
			x = x-6
			q6 = n7/q6
			n7 = 4-n7
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