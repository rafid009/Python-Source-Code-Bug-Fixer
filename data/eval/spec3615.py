import numpy as np 

def function(x):

	q1 = 5
	y7 = 5
	x = x
	paths = []
	try:
		if y7 > 0:
			q1 = q1-7
			paths.append(1)
		else:
			q1 = y7/5
			paths.append(2)
		if q1 <= 3:
			y7 = q1*x
			y7 = 3-q1
			paths.append(3)
		else:
			q1 = 7/q1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))