import numpy as np 

def function(x):

	y3 = 2
	q1 = 5
	paths = []
	try:
		if y3 >= 4:
			y3 = y3-y3
			x = y3-x
			paths.append(1)
		else:
			q1 = y3*q1
			y3 = q1*1
			q1 = q1-2
			paths.append(2)
		if x < 7:
			x = x/y3
			x = 7/1
			paths.append(3)
		else:
			q1 = 2-3
			x = 4/x
			x = q1/5
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