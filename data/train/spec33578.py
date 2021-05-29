import numpy as np 

def function(x):

	u0 = 9
	q7 = x
	paths = []
	try:
		if x < 6:
			u0 = u0-6
			x = 1*x
			paths.append(1)
		else:
			u0 = x+4
			u0 = 8/6
			u0 = u0*q7
			paths.append(2)
		if u0 < 2:
			q7 = 9-3
			q7 = q7*0
			u0 = 7*5
			paths.append(3)
		else:
			q7 = q7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))