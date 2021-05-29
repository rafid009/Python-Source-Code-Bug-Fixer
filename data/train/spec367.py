import numpy as np 

def function(x):

	q2 = 6
	c0 = x
	paths = []
	try:
		if q2 > 4:
			q2 = q2-c0
			paths.append(1)
		else:
			q2 = 8+q2
			paths.append(2)
		if q2 <= 4:
			q2 = 6+q2
			q2 = q2*9
			x = x*q2
			paths.append(3)
		else:
			c0 = x/x
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