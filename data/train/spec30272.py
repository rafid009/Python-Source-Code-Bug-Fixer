import numpy as np 

def function(x):

	d0 = 0
	q7 = x
	paths = []
	try:
		if q7 > 8:
			x = d0-x
			d0 = d0*6
			paths.append(1)
		else:
			x = x-7
			x = x+9
			paths.append(2)
		if x > 5:
			q7 = q7/4
			q7 = q7/q7
			paths.append(3)
		else:
			q7 = 1*q7
			q7 = q7*1
			d0 = d0-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))