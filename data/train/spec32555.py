import numpy as np 

def function(x):

	q7 = 2
	r9 = 0
	paths = []
	try:
		if x < 5:
			x = x*5
			q7 = q7-5
			q7 = q7*7
			paths.append(1)
		else:
			q7 = 2*q7
			paths.append(2)
		if x > 0:
			r9 = r9*6
			paths.append(3)
		else:
			r9 = q7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))