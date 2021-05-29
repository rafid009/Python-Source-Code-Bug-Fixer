import numpy as np 

def function(x):

	q1 = x
	e7 = 1
	paths = []
	try:
		if x <= 7:
			e7 = e7*2
			q1 = q1-7
			e7 = e7/7
			paths.append(1)
		else:
			q1 = 1*1
			q1 = q1-x
			e7 = e7/1
			paths.append(2)
		if e7 <= 9:
			q1 = e7*q1
			paths.append(3)
		else:
			e7 = 9+7
			q1 = q1+e7
			x = x/3
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