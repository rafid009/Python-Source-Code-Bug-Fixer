import numpy as np 

def function(x):

	q1 = x
	y6 = x
	paths = []
	try:
		if y6 < 1:
			x = x/9
			y6 = y6/7
			paths.append(1)
		else:
			y6 = y6*x
			paths.append(2)
		if x < 2:
			y6 = x/y6
			y6 = 8-4
			paths.append(3)
		else:
			x = x+8
			q1 = q1/1
			x = q1*x
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