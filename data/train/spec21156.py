import numpy as np 

def function(x):

	q7 = x
	v3 = 8
	paths = []
	try:
		if x > 5:
			q7 = q7/q7
			paths.append(1)
		else:
			q7 = q7*0
			paths.append(2)
		if x > 3:
			x = 6*x
			v3 = 9/v3
			paths.append(3)
		else:
			v3 = v3/4
			v3 = q7/v3
			q7 = q7-3
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