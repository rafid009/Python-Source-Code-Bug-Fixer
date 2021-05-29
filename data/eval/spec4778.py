import numpy as np 

def function(x):

	q1 = x
	a6 = 8
	paths = []
	try:
		if q1 < 6:
			x = x+8
			x = q1+x
			q1 = q1*q1
			paths.append(1)
		else:
			x = 6/x
			a6 = a6*8
			paths.append(2)
		if x >= 1:
			x = x+7
			a6 = q1/a6
			x = x/5
			paths.append(3)
		else:
			a6 = x*1
			a6 = a6*q1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))