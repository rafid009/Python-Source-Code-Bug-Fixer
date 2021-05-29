import numpy as np 

def function(x):

	c1 = x
	q2 = x
	paths = []
	try:
		if x > 7:
			q2 = 0-7
			x = x-c1
			q2 = q2-q2
			paths.append(1)
		else:
			q2 = 6+x
			c1 = 2/8
			c1 = x*c1
			paths.append(2)
		if x > 7:
			q2 = q2/5
			c1 = c1/7
			c1 = c1/9
			paths.append(3)
		else:
			x = 0-1
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