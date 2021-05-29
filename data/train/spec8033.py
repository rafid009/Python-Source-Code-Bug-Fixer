import numpy as np 

def function(x):

	f5 = 0
	q1 = 6
	paths = []
	try:
		if x >= 9:
			x = x*f5
			paths.append(1)
		else:
			x = q1-x
			paths.append(2)
		if f5 <= 7:
			q1 = q1/8
			paths.append(3)
		else:
			x = q1*f5
			x = 0/x
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