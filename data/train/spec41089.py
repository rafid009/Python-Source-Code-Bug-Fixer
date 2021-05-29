import numpy as np 

def function(x):

	q8 = x
	c2 = 9
	paths = []
	try:
		if x <= 1:
			c2 = c2*7
			c2 = 5*c2
			c2 = c2/2
			paths.append(1)
		else:
			q8 = q8/6
			x = x*5
			q8 = q8-0
			paths.append(2)
		if q8 < 3:
			c2 = x/c2
			x = c2-5
			c2 = 4/c2
			paths.append(3)
		else:
			q8 = x+q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))