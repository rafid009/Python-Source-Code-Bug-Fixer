import numpy as np 

def function(x):

	l8 = x
	q7 = x
	paths = []
	try:
		if x >= 5:
			q7 = q7/3
			q7 = l8+9
			paths.append(1)
		else:
			x = l8+1
			q7 = 3/3
			paths.append(2)
		if q7 < 8:
			x = q7+3
			paths.append(3)
		else:
			q7 = q7-8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		q7 = l8**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))