import numpy as np 

def function(x):

	n8 = 8
	q6 = 5
	x = x
	paths = []
	try:
		if n8 >= 3:
			q6 = q6+n8
			q6 = q6*x
			paths.append(1)
		else:
			q6 = q6+q6
			paths.append(2)
		if n8 >= 6:
			n8 = n8*n8
			x = x+q6
			q6 = q6/2
			paths.append(3)
		else:
			x = x+q6
			q6 = 6*1
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