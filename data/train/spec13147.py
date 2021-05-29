import numpy as np 

def function(x):

	q0 = 7
	y5 = 5
	paths = []
	try:
		if x > 5:
			q0 = 7/x
			q0 = q0+5
			x = x-8
			paths.append(1)
		else:
			x = y5-x
			paths.append(2)
		if y5 >= 2:
			y5 = y5+y5
			q0 = q0*7
			paths.append(3)
		else:
			y5 = y5/7
			q0 = 7/q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))