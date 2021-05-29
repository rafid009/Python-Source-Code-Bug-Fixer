import numpy as np 

def function(x):

	q2 = 6
	q7 = 0
	paths = []
	try:
		if x > 1:
			q2 = q2/6
			q2 = x-q2
			q2 = 1/q2
			paths.append(1)
		else:
			q7 = q7+7
			q2 = q7+x
			q2 = q2*x
			paths.append(2)
		if x >= 5:
			x = x+7
			q2 = q2/5
			paths.append(3)
		else:
			q7 = q7*6
			q7 = q7+1
			q7 = q7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))