import numpy as np 

def function(x):

	q1 = 0
	c7 = 7
	paths = []
	try:
		if c7 > 5:
			x = 2*x
			paths.append(1)
		else:
			x = x*7
			x = x*5
			c7 = c7+2
			paths.append(2)
		if q1 > 7:
			q1 = q1/q1
			x = 4*2
			paths.append(3)
		else:
			x = 1+x
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