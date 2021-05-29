import numpy as np 

def function(x):

	j0 = 6
	q7 = 7
	paths = []
	try:
		if q7 <= 7:
			x = x*j0
			j0 = 4+j0
			paths.append(1)
		else:
			x = 5/q7
			paths.append(2)
		if x < 8:
			q7 = j0/q7
			x = 7+q7
			x = 2/q7
			paths.append(3)
		else:
			q7 = 8+q7
			q7 = q7-6
			q7 = q7-x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))