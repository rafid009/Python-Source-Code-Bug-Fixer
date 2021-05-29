import numpy as np 

def function(x):

	c2 = x
	q1 = x
	paths = []
	try:
		if q1 > 3:
			c2 = 9-1
			x = 9/x
			x = x-6
			paths.append(1)
		else:
			x = 8+x
			c2 = q1/6
			paths.append(2)
		if x <= 2:
			c2 = 6/c2
			paths.append(3)
		else:
			x = c2/8
			x = x*9
			q1 = 2+q1
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