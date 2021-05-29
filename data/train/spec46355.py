import numpy as np 

def function(x):

	c6 = x
	q7 = x
	paths = []
	try:
		if q7 < 4:
			q7 = q7*q7
			q7 = 9*c6
			paths.append(1)
		else:
			q7 = c6+x
			q7 = x*q7
			paths.append(2)
		if x < 7:
			c6 = c6+q7
			c6 = q7*c6
			paths.append(3)
		else:
			c6 = 7+c6
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