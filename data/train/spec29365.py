import numpy as np 

def function(x):

	c4 = x
	q2 = 2
	x = x
	paths = []
	try:
		if c4 <= 9:
			x = x*1
			q2 = x/q2
			q2 = q2-1
			paths.append(1)
		else:
			c4 = c4-8
			x = x/c4
			c4 = x*c4
			paths.append(2)
		if x > 6:
			x = 8-0
			c4 = 1-2
			c4 = 1/7
			paths.append(3)
		else:
			c4 = q2-q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		q2 = q2**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))