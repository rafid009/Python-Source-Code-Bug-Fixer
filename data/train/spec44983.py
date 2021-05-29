import numpy as np 

def function(x):

	q1 = x
	u6 = 9
	paths = []
	try:
		if x >= 1:
			q1 = x/q1
			paths.append(1)
		else:
			q1 = 8+x
			u6 = u6*6
			paths.append(2)
		if q1 >= 2:
			u6 = 1+u6
			u6 = x+q1
			u6 = 8*u6
			paths.append(3)
		else:
			x = x+x
			x = x-4
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