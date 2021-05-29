import numpy as np 

def function(x):

	u0 = x
	q1 = x
	x = x
	paths = []
	try:
		if x >= 9:
			x = 4/x
			q1 = x*q1
			paths.append(1)
		else:
			q1 = x/9
			paths.append(2)
		if u0 <= 2:
			u0 = 6/1
			paths.append(3)
		else:
			u0 = 0-u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		q1 = u0**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))