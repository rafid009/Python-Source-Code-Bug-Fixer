import numpy as np 

def function(x):

	q1 = x
	c5 = 8
	paths = []
	try:
		if x >= 0:
			q1 = q1*c5
			x = 7-x
			x = x/x
			paths.append(1)
		else:
			x = q1*x
			c5 = x*q1
			paths.append(2)
		if x >= 6:
			q1 = 8+1
			c5 = 5*c5
			x = 7*x
			paths.append(3)
		else:
			c5 = c5+7
			x = x-0
			q1 = 2-q1
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		q1 = c5**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))