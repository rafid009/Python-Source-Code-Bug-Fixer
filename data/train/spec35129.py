import numpy as np 

def function(x):

	q1 = 7
	g3 = 4
	paths = []
	try:
		if x >= 1:
			q1 = q1/x
			x = 0/x
			x = x+q1
			paths.append(1)
		else:
			g3 = g3+0
			g3 = 7+6
			q1 = q1-2
			paths.append(2)
		if x < 2:
			q1 = q1-4
			paths.append(3)
		else:
			q1 = 3-9
			q1 = q1+7
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))